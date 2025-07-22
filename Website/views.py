from django.shortcuts import render,HttpResponse,redirect
from .models import Item
from django.http import JsonResponse
import subprocess
import os
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def homepage(request):
    return render(request,'index.html')

def Movies(request):
    return render(request,'movies.html')

def Trailers(request):
    return render(request,'trailers.html')

def News(request):
    return render(request,'News.html')

def Songs(request):
    return render(request,'music.html')

def Movie1(request):
    return render(request,'movie1.html')

def Movie2(request):
    return render(request,'movie2.html')

def Movie3(request):
    return render(request,'movie3.html')

def Movie4(request):
    return render(request,'movie4.html')

def Movie5(request):
    return render(request,'movie5.html')

def Movie6(request):
    return render(request,'movie6.html')

def playlist1(request):
    return render(request,'playlist1.html')

def playlist2(request):
    return render(request,'playlist2.html')

def playlist3(request):
    return render(request,'playlist3.html')

def playlist4(request):
    return render(request,'playlist4.html')

def playlist5(request):
    return render(request,'playlist5.html')

def playlist6(request):
    return render(request,'playlist6.html')

def video(request):
    obj = Item.objects.all()
    return render(request,'trailers.html',{'obj':obj})

def Stories(request):
    return render(request ,'Stories.html')

def Horror(request):
    return render(request,'Horror.html')

def Thriller(request):
    return render(request,'Thriller.html')

def Mystery(request):
    return render(request,'Mystery.html')

def Science_Fiction(request):
    return render(request,'Science_Fiction.html')

def Adventure(request):
    return render(request,'Adventure.html')

def Action(request):
    return render(request,'Action.html')

def Fantasy(request):
    return render(request,'Fantasy.html')

def Games(request):
    return render(request,'Games.html')

def hstory1(request):
    return render(request,'The_Yellow_Wall_paper.html')

def hstory2(request):
    return render(request,'The Birds1.html')

def hstory3(request):
    return render(request,'The Tell-Tale Heart.html')

def hstory4(request):
    return render(request,'the cask of Amontillado1.html')

def hstory5(request):
    return render(request,'The landlady1.html')

def hstory6(request):
    return render(request,'The lottery.html')

def hstory7(request):
    return render(request,'The most Dangerous Game1.html')

def hstory8(request):
    return render(request,'The Monkeys paw1.html')

def hstory9(request):
    return render(request,'The open winndow1.html')

def mystery1(request):
    return render(request,'mystery1.html')

def mystery2(request):
    return render(request,'mystery2.html')

def mystery3(request):
    return render(request,'mystery3.html')

def mystery4(request):
    return render(request,'mystery4.html')

def mystery5(request):
    return render(request,'mystery5.html')

def sf1(request):
    return render(request,'sf1.html')

def sf2(request):
    return render(request,'sf2.html')

def sf3(request):
    return render(request,'sf3.html')

def sf4(request):
    return render(request,'sf4.html')

def sf5(request):
    return render(request,'sf5.html')

def sf6(request):
    return render(request,'sf6.html')

def ad1(request):
    return render(request,'ad1.html')

def ad2(request):
    return render(request,'ad2.html')

def ad3(request):
    return render(request,'ad3.html')

def ad4(request):
    return render(request,'ad4.html')

def ad5(request):
    return render(request,'ad5.html')

def ac1(request):
    return render(request,'ac1.html')

def ac2(request):
    return render(request,'ac2.html')

def ac3(request):
    return render(request,'ac3.html')

def ac4(request):
    return render(request,'ac4.html')

def ac5(request):
    return render(request,'ac5.html')

def f1(request):
    return render(request,'f1.html')

def f2(request):
    return render(request,'f2.html')

def f3(request):
    return render(request,'f3.html')

def f4(request):
    return render(request,'f4.html')

def f5(request):
    return render(request,'f5.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pas = request.POST.get('password')
        user = authenticate(request,username=username,password = pas)
        if user is not None:
            login(request,user)
            return redirect('home') 
        else:
            return HttpResponse("Username or Password is invalid") 
    return render(request,'login.html')



def SignUp(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')

        my_user = User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')
        
        
    return render(request,'signup.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

import subprocess
from django.http import JsonResponse
import os
from django.conf import settings

def launch_game(request, game_name):
    game_scripts = {
        'brick_breaker': os.path.join(settings.BASE_DIR, 'static', 'brick_breaker.py'),
        'connect': os.path.join(settings.BASE_DIR, 'static', 'connect.py'),
        'tictactoe': os.path.join(settings.BASE_DIR, 'static', 'tictactoe.py'),
        'guess_the_word': os.path.join(settings.BASE_DIR, 'static', 'guess_the_word.py'),
        'mines': os.path.join(settings.BASE_DIR, 'static', 'minesweeper.py'),
        'connect': os.path.join(settings.BASE_DIR, 'static', 'connect.py'),
        'sudoku':os.path.join(settings.BASE_DIR, 'static', 'sudoku.py'),
        'maze':os.path.join(settings.BASE_DIR, 'static', 'maze.py'),
        'memory_game':os.path.join(settings.BASE_DIR, 'static', 'memory_game.py'),
        'game1': os.path.join(settings.BASE_DIR, 'static', 'game1.py'),#2048
        'game2': os.path.join(settings.BASE_DIR, 'static', 'game2.py'),#Ballon shooter
        'game3': os.path.join(settings.BASE_DIR, 'static', 'game3.py'),#snake
        'game4': os.path.join(settings.BASE_DIR, 'static', 'game4.py'),#wordsearch
        'game5': os.path.join(settings.BASE_DIR, 'static', 'game5.py'),#pong
        'game6': os.path.join(settings.BASE_DIR, 'static', 'game6.py'),#quiz

    }
    script_path = game_scripts.get(game_name)

    if script_path:
        subprocess.Popen(['python', script_path])
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Game not found'}, status=404)
