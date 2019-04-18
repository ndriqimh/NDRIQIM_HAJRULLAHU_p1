from socket import *


#emriServerit = 'localhost'
#portiServerit = 12000
klientSoketi = socket(AF_INET,SOCK_STREAM)
emriServerit = input('Shenoni emrin e serverit: ')
portiServerit = int(input('Shenoni portin e serverit: '))

if (portiServerit>=1024 and portiServerit<=65535):
    klientSoketi.connect((emriServerit, portiServerit))
    print('Jeni lidhur me serverin\n')
else:
    print('Shenoni portin mes kufive te caktuar')

print('========================================================================================================================')
print('Serveri mund te kryej keto Operacione: IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, PRINTIMI,' 
'\n\t\t\t\t\tEMRIIKOMPJUTERIT, KOHA, LOJA, FIBONACCI, KONVERTIMI,SFERA,TRAPEZI')
print('========================================================================================================================')
print('1.IPADRESA kthen  Ipadresen e serverit.\n2.NUMRIIPORTIT kthen portin e serverit.'
      '\n3.BASHKETINGELLORE kthen numrin e bashtinglloreve te shenuara nga nje fjali.Sheno {HAPSIRE} teksti:'
      '\n4.PRINTIMI kthen fjaline e shtypur.Sheno {HAPSIRE} tekst.\n5.EMRIIKOMPJUTERIT kthen emrin e kompjuterit.'
      '\n6.KOHA kthen kohen(oren).''\n7.Operacioni LOJA kthen numrat e rastit nga 1-49.'
      '\n8.FIBONACCI kthen shumen e numrave fibonacci.Sheno {Hapsirë} Numër'
      '\n9.KONVERTIMI konverton njesit.''Lista e parametrave te KONVERTIMI janë:[KilowattToHorsepower,'
      'HorsepowerToKilowatt,''\n\t\t\t\t\t\tDegreesToRadians,RadiansToDegrees,GallonsToLiters,LitersToGallons]'
      '\n\t\t\t\t\t\tSheno {Hapsirë} Opcioni {Hapsirë} Numër'
      '\n10.SFERA kthen vellimin e sferes.Sheno SFERA {Hapsirë} Numër(Rrezja)'
      '\n11.TRAPEZI kthen syprinen e trapezit.Sheno SFERA {Hapsirë} Numër(Lartesia) {Hapsirë} Numër(Baza1) {Hapsirë} Numër(Baza2)'
      
      '\nSheno Perfundo per te mbyllur lidhjen me serverin')
print('========================================================================================================================')
while True:
    #inputi qe shenohet nga klienti se qka deshiron
    fjaliaHyrese = input('Shenoni njerin nga opsionet qe deshironi ta zgjidhni: ')
    #dergimi ne server ,gjithqka qe dergohet duhet te enkodohet
    klientSoketi.sendall(fjaliaHyrese.encode())
    #fjalia qe pranohet nga serveri
    fjaliaPranuar = klientSoketi.recv(128)
    print("Nga serveri " + fjaliaPranuar.decode())
    if(fjaliaHyrese == 'Perfundo'):
        print("Keni mbyllur lidhjen me serverin.Diten e mire")
        break
klientSoketi.close()
