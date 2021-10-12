#faça um programa abra e reproduza um audio e arquivo mp3.

from pygame import mixer
mixer.init()
mixer.music.load("Insonia.mp3")
mixer.music.play()
input("Aperte enter para sair")