from multiprocessing import context
from django.shortcuts import render, redirect
from base.models import *
from PIL import Image, ImageDraw, ImageFont
import random
import os
from django.conf import settings

def home(request):
    context = {
        'temp' : Template.objects.all()
    }
    return render(request, 'base.html', context)

def selected(request, uid):
    gi = Template.objects.get(uid=uid)
    print(gi.image.url)

    context = {
        'temp' : Template.objects.all(),
        'photo' : gi
    }
    return render(request, 'base.html', context)

def generate(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        tid = request.POST.get('tempid')

        get_temp = Template.objects.get(uid=tid)

        img = Image.open(f'{settings.BASE_DIR}{get_temp.image.url}')
        drew = ImageDraw.Draw(img)
        font = ImageFont.truetype("comicbd.ttf", 50)
        drew.text((50, 30), text, font=font, fill=(255,0,0))
        name = random.randint(100000,999999)
        img.save(f"{settings.BASE_DIR}/media/{name}.png")
        context = {
            'name' : name,
            'temp' : Template.objects.all(),
        }
        return render(request, 'base.html', context)
