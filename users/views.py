from django.shortcuts import render
import serial


def getsensordata():
    print("------Reading collection starts now------")
    sr = serial.Serial("/dev/ttyACM0", 9600)
    st = list(str(sr.readline(), 'utf-8'))
    sr.close()
    print("------Reading collection ends successfully------")
    return float(str(''.join(st[:])))


def index(request):
    return render(request, 'start.html', {'temp': getsensordata()})
