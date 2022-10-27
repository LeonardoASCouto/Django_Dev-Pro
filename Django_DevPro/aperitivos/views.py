from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': 760589226},
        'instalacao': {'titulo': 'Vídeo Aperitivo: Instalacao', 'vimeo_id': 764688138}
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
