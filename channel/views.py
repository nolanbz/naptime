from django.shortcuts import render

def video_list(request):
    return render(request, 'channel/video_list.html', {})
