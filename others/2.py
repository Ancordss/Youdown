from youtube import PlayList
import concurrent.futures

from youtube.__main__ import Video




def navigation():


    navigation_eingabe = int(input("ingresa un numero: "))


    if navigation_eingabe == 1:
        down()
    if navigation_eingabe == 2:
        exit()
    else:
        print("Give me a a 1/2")



def down():
    link=str(input("introduce el link: "))
    v = Video(link).streams
    v.fflow.download()

navigation()


    
