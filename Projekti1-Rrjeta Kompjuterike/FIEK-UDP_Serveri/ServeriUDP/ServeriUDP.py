from socket import *
import random,datetime


emriServerit ="localhost"
portiServerit  = 12000
soketiServerit = socket(AF_INET, SOCK_DGRAM)
soketiServerit.bind((emriServerit, portiServerit))
print('Serveri eshte gati per te pranuar kerkesa nga klienti.')

#Operacionet e kerkuara ne Projekt
def IPADRESA():
    return str(adresaKlientit[0])
def NUMRIIPORTIT():
    return str(adresaKlientit[1])
def BASHKETINGELLORE(tekstiDhene):
    shkronjatB = ['B','b','C','c','D','d','F','f','G','g','H','h','J','j','K','k','L','l','M','m','N','n','P','p','Q','q','R','r','S','s',
                  'T','t','V','v','X','x','W','w','Y','y','Z','z']
    counteri=0;
    for i in str(tekstiDhene):
        if i in shkronjatB:
            counteri+=1

    return str(counteri)
def PRINTIMI(fjaliaHyrese):
    fjaliaHyrese=str(fjaliaHyrese).strip()
    return str(fjaliaHyrese)
def EMRIKOMPJUTERIT():
    try:
        emriHostit = gethostname()
        return str(emriHostit)
    except socket.error as gabim:
        print('Emri i hostit nuk egziston ose nuk gjindet')
def KOHA():
    dataTanishme = datetime.datetime.now()
    return dataTanishme
def LOJA():
    return (random.sample(range(1, 49), 7))
def FIBONACCI(variablaHyrese):
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
def KONVERTIMI(zgjedhja,sasia):
    if(zgjedhja == 'KilowattToHorsepower'):
        return(float(sasia*1.34102))
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
def SFERA(rrezja):
    PI = 3.14
    Vellimi = (4 / 3) * PI * rrezja * rrezja * rrezja
    return  Vellimi
def TRAPEZI(lartesia,baza1,baza2):
    Syprina = ((baza1 + baza2) / 2) * lartesia
    return Syprina

while 1:
       
        fjaliaArdhur=(bytes)("fjalia string ".encode())
        try:

            while str(fjaliaArdhur.decode()) != "":
                try:

                    fjaliaArdhur ,adresaKlientit = soketiServerit.recvfrom(128)
                    
                    fjaliaDekoduar = fjaliaArdhur.decode()
                    fjaliaM =fjaliaDekoduar
    
                    fjaliaM  = fjaliaM .split (" ") 
                    fjaliaErradhes="".join(fjaliaM[1:])
                    fjaliaJoin=" ".join(fjaliaM[1:])
                except:
                    print('Klienti ka kerkuar' + fjalia.decode())

                if (fjaliaM[0] == 'IPADRESA'):
                    var  = IPADRESA();
                    dergimi  = ('Ip eshte: '+ str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)             
                elif (fjaliaM[0] == 'NUMRIIPORTIT'):
                    var = NUMRIIPORTIT()
                    dergimi = ('Numri i portit eshte: ' + str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit) 
                elif (fjaliaM[0] == 'BASHKETINGELLORE'):
                    var = BASHKETINGELLORE(fjaliaErradhes)
                    dergimi = ('Numri i bashketinglloreve eshte: ' + str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)
                elif (fjaliaM[0] == 'PRINTIMI'):
                    var = PRINTIMI(fjaliaJoin)
                    dergimi = ('Printimi i tekstit eshte: '+str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)
                elif (fjaliaM[0] == 'EMRIIKOMPJUTERIT'):
                    var = EMRIKOMPJUTERIT()
                    dergimi = ('Emri i kompjuterit eshte:'+str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)
                elif (fjaliaM[0] == 'KOHA'):
                    var = KOHA()
                    dergimi = ('Koha e tanishme ne kompjuter eshte: ' +str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)      
                elif (fjaliaM[0] == 'LOJA'):
                    var = LOJA()
                    dergimi = ('Numrat e gjeneruar te rastit jane: ' +str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)          
                elif (fjaliaM[0] == 'FIBONACCI'):
                    var =  FIBONACCI(fjaliaM[1])
                    dergimi = ('Numri fibonacci eshte: '+str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)        
                elif (fjaliaM[0] == 'KONVERTIMI'):
                    var = KONVERTIMI(str(fjaliaM[1]),float(fjaliaM[2]))
                    dergimi = ('Konvertimi qe keni kerkuar eshte: ' +str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)  
                elif (fjaliaM[0] == 'SFERA'):
                    var = SFERA(float(fjaliaM[1]))
                    dergimi = ('Vellimi i sferes eshte: ' +str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)
                elif (fjaliaM[0] == 'TRAPEZI'):
                    var = TRAPEZI(float(fjaliaM[1]),float(fjaliaM[2]),float(fjaliaM[3]))
                    dergimi = ('Syrina e trapezit eshte: ' +str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)

                else:
                    serverSocket.sendto('Operacioni qe keni zgjedhur nuk eshte ne rregull.Rishkruani perseri',adresaKlientit)
       
        except Exception as gabim:
            print('Klienti ka shtypur diqka gabim ose ka mbyllur lidhjen')
            
    
