from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL
import string, random

from django.shortcuts import render, redirect
from .models import ShortURL

def generate_shortcode(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def home(request):
    short_url = None
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        shortcode = generate_shortcode()
        ShortURL.objects.create(long_url=long_url, shortcode=shortcode)
        short_url = request.build_absolute_uri(f'/{shortcode}/')
    return render(request, 'home.html', {'short_url': short_url})

def redirect_url(request, shortcode):
    url = get_object_or_404(ShortURL, shortcode=shortcode)
    return redirect(url.long_url)
