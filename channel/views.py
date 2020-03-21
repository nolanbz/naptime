from django.shortcuts import render
from django.utils import timezone
from .models import Channel

def channel_list(request):
    channels = Channel.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'channel/channel_list.html', {'channels': channels})
