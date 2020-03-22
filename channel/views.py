from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Channel
from .forms import ChannelForm


def channel_list(request):
    channels = Channel.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'channel/channel_list.html', {'channels': channels})

def channel_detail(request, pk):
    channel = get_object_or_404(Channel, pk=pk)
    return render(request, 'channel/channel_detail.html', {'channel': channel})

def channel_new(request):
    if request.method == "POST":
        form = ChannelForm(request.POST)
        if form.is_valid():
            channel = form.save(commit=False)
            channel.author = request.user
            channel.published_date = timezone.now()
            channel.save()
            return redirect('channel_detail', pk=channel.pk)
    else:
        form = ChannelForm()
    return render(request, 'channel/channel_edit.html', {'form': form})

def channel_edit(request, pk):
    channel = get_object_or_404(Channel, pk=pk)
    if request.method == "POST":
        form = ChannelForm(request.POST, instance=channel)
        if form.is_valid():
            channel = form.save(commit=False)
            channel.author = request.user
            channel.published_date = timezone.now()
            channel.save()
            return redirect('channel_detail', pk=channel.pk)
    else:
        form = ChannelForm(instance=channel)
    return render(request, 'channel/channel_edit.html', {'form': form})