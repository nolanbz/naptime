from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Channel

def channel_list(request):
    channels = Channel.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'channel/channel_list.html', {'channels': channels})

def channel_detail(request, pk):
    channel = get_object_or_404(Channel, pk=pk)
    return render(request, 'channel/channel_detail.html', {'channel': channel})