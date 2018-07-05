import datetime

now = datetime.datetime.now()
import os
def ta(th,tm, song):
    ls=True
    if(ls):
        a = now.hour
        b = now.minute
        if(a==th):
            if(b==tm):
                
                os.system("cd music")
                
                pl = "start " + song
                os.system(pl)

                
#take time
th = input("hour :-")
tm = input("minute :-")


song = input("Song Name:- ")
ta(th,tm,song)
