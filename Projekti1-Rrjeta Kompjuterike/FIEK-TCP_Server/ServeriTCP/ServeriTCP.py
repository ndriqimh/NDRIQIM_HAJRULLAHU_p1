from socket import *
import random, datetime
from _thread import *

emriServerit = 'localhost'
portiServerit = 12000
s = socket(AF_INET,SOCK_STREAM)

try:
    #vendosja e lidhjes me serverin
    s.bind((emriServerit,portiServerit))
except s.error as gabim:
    print('E pamundur per tu lidhur me serverin' + str(gabim))
#Ndegjimi i serverit per te pranuar klient 
s.listen(5)
print('Serveri eshte gati per te pranuar kerkesa nga klienti.')

#Operacionet e kerkuara ne Projekt
def ipAdresa():
    return str(addr[0])
def numriPortit():
    return str(addr[1])
def bashketingllore(tekstiDhene):
    shkronjatB = ['B','b','C','c','D','d','F','f','G','g','H','h','J','j','K','k','L','l','M','m','N','n','P','p','Q','q','R','r','S','s',
                  'T','t','V','v','X','x','W','w','Y','y','Z','z']
    counteri=0;
    for i in str(tekstiDhene):
        if i in shkronjatB:
            counteri+=1

    return str(counteri)
def printimi(fjaliaHyrese):
    fjaliaHyrese=str(fjaliaHyrese).strip()
    return str(fjaliaHyrese)
def emriKompjuterit():
    try:
        emriHostit = gethostname()
        return str(emriHostit)
    except socket.error as gabim:
        print('Emri i hostit nuk egziston ose nuk gjindet')
def koha():
    dataTanishme = datetime.datetime.now()
    return dataTanishme
def loja():
    return (random.sample(range(1, 49), 7))
def fibonacci(variablaHyrese):
    a,b=1,0
    try:
        shikimi=int(variablaHyrese)
    except:
        print('Numri i dhene duhet te jete vetem integjer')
    if(shikimi<=0):
        print('Numri duhet te jete pozitiv')
    for i in range(shikimi-1):
        a=a+b
        b=a-b
    return str(a)
def konvertimi(zgjedhja,sasia):
    if(zgjedhja == 'KilowattToHorsepower'):
        return(float(sasia/1.34102))
    elif(zgjedhja == 'HorsepowerToKilowatt'):
        return(float(sasia*0.7457))
    elif(zgjedhja == 'DegreesToRadians'):
        return(float(sasia*0.0174533))
    elif(zgjedhja == 'RadiansToDegrees'):
        return(float(sasia*57.2958))
    elif(zgjedhja == 'GallonsToLiters'):
        return(float(sasia*3.78541))
    elif(zgjedhja == 'LitersToGallons'):
        return(float(sasia*0.264172))
    else:
        return('Keni shtypur diqka gabim')
#Operacionet e zgjedhura 
def sfera(rrezja):
    PI = 3.14
    Vellimi = (4 / 3) * PI * rrezja * rrezja * rrezja
    return  Vellimi
def trapezi(lartesia,baza1,baza2):
    Syprina = ((baza1 + baza2) / 2) * lartesia
    return Syprina

#funksioni per multithread
def thread_klientat():
    while 1:
        
        print('Klienti u lidh ne serverin %s me port %s' % addr)   
        fjaliaArdhur=(bytes)("fjalia string".encode())
        
        try:

            while str(fjaliaArdhur.decode()) != "":

                try:
                    
                    fjaliaArdhur = connectionSocket.recv(1024)
                    
                    fjaliaDekoduar = fjaliaArdhur.decode()
                    
                    fjaliaM = fjaliaDekoduar

                    fjaliaM = fjaliaM.split(" ")
                    fjaliaErradhes="".join(fjaliaM[1:]) 
                    fjaliaJoin=" ".join(fjaliaM[1:]) 
                except:
                    print('Klienti ka kerkuar' + fjalia.decode())

                
                if (fjaliaM[0] == 'IPADRESA'):
                    var = ipAdresa()
                    dergimi = ('Ip eshte: '+ str(var))

                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'NUMRIIPORTIT'):
                    var = numriPortit()
                    dergimi = ('Numri i portit eshte: ' + str(var))

                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'BASHKETINGELLORE'):
                    var = bashketingllore(fjaliaErradhes)
                    dergimi = ('Numri i bashketinglloreve eshte: ' + str(var))
                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'PRINTIMI'):
                    var = printimi(fjaliaJoin)
                    dergimi = ('Printimi i tekstit eshte: '+str(var))
                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'EMRIIKOMPJUTERIT'):
                    var = emriKompjuterit()
                    dergimi = ('Emri i kompjuterit eshte:'+str(var))
                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'KOHA'):
                    var = koha()
                    dergimi = ('Koha e tanishme ne kompjuter eshte: ' +str(var))
                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'LOJA'):
                    var = loja()
                    dergimi = ('Numrat e gjeneruar te rastit jane: ' +str(var))
                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'FIBONACCI'):
                    var =  fibonacci(fjaliaM[1])
                    dergimi = ('Shuma e numrave fibonacci eshte: '+str(var))
                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'KONVERTIMI'):
                    var = konvertimi(str(fjaliaM[1]),float(fjaliaM[2]))
                    dergimi = ('Konvertimi qe keni kerkuar eshte: ' +str(var))
                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'SFERA'):
                    var = sfera(float(fjaliaM[1]))
                    dergimi = ('Vellimi i sferes eshte: ' +str(var))
                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'TRAPEZI'):
                    var = trapezi(float(fjaliaM[1]),float(fjaliaM[2]),float(fjaliaM[3]))
                    dergimi = ('Syrina e trapezit eshte: ' +str(var))
                    connectionSocket.send(dergimi.encode())
                else:
                    connectionSocket.send('Operacioni qe keni zgjedhur nuk eshte ne rregull.Rishkruani perseri'.encode())
            connectionSocket.close()
        except Exception as g:
            print("Klienti ka shtypur diqka gabim ose ka mbyllur lidhjen")
            break
while True:
     connectionSocket, addr = s.accept()
     start_new_thread(thread_klientat)
connectionSocket.close()

