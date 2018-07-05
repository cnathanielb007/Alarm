import datetime

now = datetime.datetime.now()
import os
def call(song):
    os.system("cd music")
    pl = "start " + song
    os.system(pl)
def ta(th,tm, song):
    ls=True
    if(ls):
        a = now.hour
        b = now.minute
        if(a==th):
            if(b==tm):
                call(song)

                
#take time
th = input("hour :-")
tm = input("minute :-")


song = input("Song Name:- ")
ta(th,tm,song)
