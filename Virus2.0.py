import time
import os
import platform
import math
#Comando para limpiar la pantalla.
def cls():
    if platform.system()=="Windows":
        os.system("cls")
    else:
        os.system("clear") 
cls()
#hace operaciones necesarias para el resto de funciones.
def HostMenor(deber,agber):
    deber=int(deber)
    agber=int(agber)
    va, result, vava = (0,0,0)
    for i in range(deber):
        vava+=1
        va+=1
        if va==1:
            result+=128
        elif va==2:
            result+=64
        elif va==3:
            result+=32
        elif va==4:
            result+=16
        elif va==5:
            result+=8
        elif va==6:
            result+=4
        elif va==7:
            result+=2
        elif va==8:
            result+=1
        elif va==9:
            print(" 255 ", end="   ")
            va=1
            result=0
            result+=128
        print(1, end=" ")
        if vava==9:
            vava=1 
    if va==8:
        print("  ", result, end="   ")
    canon=0
    valores=0
    caa=10
    for o in range(agber):
        vava+=1
        canon+=1
        print(0, end=" ")
        if valores==0:
            if va<8 and canon==8-va:
                print(end="  ")
                print( result, end="   ")
                caa=1
                valores=1
        if vava==9:
            vava=1 
        if caa==1:
            caa=0
        elif caa==0:
            if vava==8:
                print(" ", "0 ", end="  ")    
    result=int(result)
#De Números a bits.             4         (este está bien optimizado entre comillas xd)
def test0002():
    aper=int(input("Ingresa el número que desees: " ))
    restante33=aper
    variables44=""
    while restante33>0:
        if restante33%2==0:
            variables44+=" 0"
        else:
            variables44+=" 1"
        restante33=math.floor(restante33/2)
    print("Resultado:",variables44[::-1],"\n")
def NumToBits():
    efex="sí"
    while efex=="sí" or efex=="si":
        test0002()
        efex=input("Deseas hacer más cálculos?\nsí\\no: ")
        if efex=="si" or efex=="sí":
            cls()
        else:
            cls()
#De bits a Números.             2
def BitsToNum():
    ifex="sí"
    while ifex=="sí" or ifex=="si":
        posi1="0" 
        Ma=input("Ingresa los números en binario: ")
        maInvert=Ma[::-1]
        conteo001=0
        resuu=int(0)
        for sd in maInvert:
            conteo001+=1
            posi1=int(sd)
            resuu+=posi1*(2**(conteo001-1))
        print("\nResultado: ", end="")
        for asdjkh in Ma: 
            print(asdjkh, end=" ")
        print("   ",resuu,"\n")
        ifex=str(input("Deseas hacer más cálculos?\nsí\\no: "))
        if ifex=="si" or ifex=="sí":
            cls()
        else:
            cls()   
#De bits de red a dirección     1
def DeBitsDeRed():
    ifxx="sí"
    while ifxx=="sí" or ifxx=="si":
        host=0        
        exponente=300
        while exponente>32:
            exponente=int(input("Ingresa el número de Bits de red: "))
            Número_de_bits_prestados=int(32-exponente)
        if host==0:
            HostMenor(exponente,Número_de_bits_prestados)
        else:
            host=0
        ifxx=str(input("\n \nDeseas hacer más cálculos?\nsí\\no: "))
        if ifxx=="si" or "sí":
            cls()
#función para imprimir las subredes con los espacios necesarios para que queden perfectamente alineadas.
def Imprimir_and_space(resultado):
    Espacios_totales=''
    Suma_de_espacios=0
    Espacios=resultado
    Sin_Puntos=''
    for total in Espacios:
        if total=='.':
            total=''
        Sin_Puntos+=total
    for T2 in Sin_Puntos:
        Suma_de_espacios+=1
    Restando=16-Suma_de_espacios
    for x in range(Restando):
        Espacios_totales+=' '
    print(resultado,Espacios_totales, end="")
#Sistemam de suma en distintos octetos.
def Suma_Octetos(octetos, P1,P2,P3,P4,interador):
    P1=int(P1)
    P2=int(P2)
    P3=int(P3)
    P4=int(P4)
    for i in range(octetos):
        P4+=1
        if P4>255:
            P4=0
            P3+=1
            if P3>255:
                P3=0
                P2+=1
                if P2>255:
                    P2=0
                    P1+=1
    if interador==1:
        Espacio_de_prueba=12
    elif interador==0:
        Imprimir_and_space(str(P1)+'.'+str(P2)+'.'+str(P3)+'.'+str(P4))
    return (str(P1),str(P2),str(P3),str(P4))
#División de redes(incompleto)  3
def division_redes():
    lhjdfis=1
    while lhjdfis==1:
        Dirección=input('Ingresa tu ip: ')
        Valor_en_blanco=('','','','')
        P1, P2, P3, P4=Valor_en_blanco
        suma=0
        for e in Dirección:
            if e=='.':
                suma+=1 
                e=''
            if suma==0:
                P1+=e
            elif suma==1:
                P2+=e
            elif suma==2:
                P3+=e
            elif suma==3:
                P4+=e   
        print(P1,'.',P2,'.',P3,'.',P4,'\n')
        if P1=='' or P2=='' or P3=='' or P4=='':
            print("El valor ingresado está fuera de rango")
            break
        else:
            P1=int(P1)
            P2=int(P2)
            P3=int(P3)
            P4=int(P4)
        if P1<=0 or P1>=224:
            print("El valor ingresado está fuera de rango")
            break
        host=input("Ingresa el número de hosts deseados: ")
        if host=='':
            print('Valor fuera de rango')
            break 
        else:
            host=int(host)
        print("\n")
        #Imprime el tipo de red y calcula los números necesarios para luego calcular el número de red personalizada.
        if host>0:
            if P1<=127:
                print("Su red es de tipo A") 
                print("Tu mascara de subred por defecto es: 255.0.0.0")
                valor=24
            elif P1<=191:
                print("Su red es de tipo B")
                print("Tu mascara de subred por defecto es: 255.255.0.0")
                valor=16
            elif P1<=223:
                print("Tu red es de tipo C")
                print("Tu mascara de subred por defecto es: 255.255.255.0")
                valor=8
            exponente=math.ceil(math.log2(host+2))
            número_de_hosts_totales=2**exponente
            número_de_hosts_utilizables=número_de_hosts_totales-2
            Número_de_bits_prestados=valor-exponente
            Número_total_de_subredes=2**Número_de_bits_prestados
            print("Subredes totales:", Número_total_de_subredes)
            print("Hosts totales:", número_de_hosts_totales)
            print("Hosts utilizables:", número_de_hosts_utilizables)
            print("Bits prestados:", Número_de_bits_prestados)
            print("\nInformación necesaria: \n128 64 32 16 8 4 2 1\n")
            print("Bits red",Número_de_bits_prestados)
            print("Bits host:",exponente,"\n")
        else:
            red=input("Ingresa el número de redes deseadas: ")
            if red=='':
                print('Valor fuera de rango')
                break
            else:
                red=int(red)
            inicio=time.time()
            print("\n")
            if P1<=127:
                print("Su red es de tipo A") 
                print("Tu mascara de subred por defecto es: 255.0.0.0")
                valor=24
            elif P1<=191:
                print("Su red es de tipo B")
                print("Tu mascara de subred por defecto es: 255.255.0.0")
                valor=16
            elif P1<=223:
                print("Tu red es de tipo C")
                print("Tu mascara de subred por defecto es: 255.255.255.0")
                valor=8
            else:
                print("Fuera de rango")
                exit()
            exponente=math.ceil(math.log2(red))
            número_de_hosts_totales=2**exponente
            Número_de_bits_prestados=valor-exponente
            Número_total_de_subredes=2**Número_de_bits_prestados
            número_de_hosts_utilizables=Número_total_de_subredes-2
            print("Subredes totales:", número_de_hosts_totales)
            print("Hosts totales:", Número_total_de_subredes)
            print("Hosts utilizables:", número_de_hosts_utilizables)
            print("Bits prestados:", exponente)
            print("\nInformación necesaria: \n128 64 32 16 8 4 2 1\n")
            print("Bits red",exponente)  
            print("Bits host:",Número_de_bits_prestados,"\n")
        #Calcula la dirección.
        if host>0:
            HostMenor(Número_de_bits_prestados,exponente)
            print("")
        else:
            HostMenor(exponente,Número_de_bits_prestados)
            print("")
        if host>0:
            suma=número_de_hosts_totales
            suma=int(suma)
        else: 
            suma=Número_total_de_subredes
            suma=int(suma)
        def Primera_Subred(Sumatoria,c1,c2,c3,c4,iterador):
            print("1", end='       ')
            if iterador==1:
                caché=(Suma_Octetos(Sumatoria,c1,c2,c3,c4,1))
            elif iterador==0:
                Suma_Octetos(0,c1,c2,c3,c4,0)
                Suma_Octetos(1,c1,c2,c3,c4,0)
                Ultima_dirección=Sumatoria-2
                Suma_Octetos((Ultima_dirección),c1,c2,c3,c4,0)
                Suma_Octetos((Ultima_dirección+1),c1,c2,c3,c4,0)
                caché=0
            return caché
        print('')
        def Total_Suma(Sumatoria,c1,c2,c3,c4,iterador):
            if iterador==1:
                Sobras=(Suma_Octetos(Sumatoria,c1,c2,c3,c4,1))
            elif iterador==0:
                Suma_Octetos((Sumatoria),c1,c2,c3,c4,0)
                Suma_Octetos((Sumatoria+1),c1,c2,c3,c4,0)
                Ultima_dirección=suma-3
                Suma_Octetos((Sumatoria+1+Ultima_dirección),c1,c2,c3,c4,0)
                Suma_Octetos((Sumatoria+Ultima_dirección+2),c1,c2,c3,c4,0)
                Sobras=0
            return Sobras
        print('')
        Cantidad_de_Subredes=input("Ingresa la cantidad de subredes deseadas: ")
        if Cantidad_de_Subredes=='':
            print('Fuera de rango')
            break
        else:
            Cantidad_de_Subredes=int(Cantidad_de_Subredes)
        print('')
        Primera_Subred(suma,P1,P2,P3,P4, 0)
        print('')
        inicio=time.time()
        multiplicador_subredes=0
        Posición_subred=2
        for Cantidad in range(Cantidad_de_Subredes):
            if Cantidad==0:
                multiplicador_subredes+=1
                Posición_subred=1
            else:
                if Posición_subred>999:
                    print(Posición_subred, end='    ')
                elif Posición_subred>99:
                    print(Posición_subred, end='     ')
                elif Posición_subred>9:
                    print(Posición_subred, end='      ')
                elif Posición_subred>=0:
                    print(Posición_subred, end='       ')
                else:
                    print(Posición_subred, end='  ')
                Total_Suma(suma,P1,P2,P3,P4, 0)
                if Cantidad==0:
                    P1,P2,P3,P4=(Primera_Subred(suma,P1,P2,P3,P4, 1))
                elif Cantidad>0 and Cantidad<Cantidad_de_Subredes+1:
                    P1,P2,P3,P4=(Total_Suma(suma,P1,P2,P3,P4, 1))
                print('')
            Posición_subred+=1
        finall=time.time()
        timer=finall-inicio
        print(f"\nTiempo de calculo: {round(timer,2)} segundos.")
        input('')        
        cls()
elec0002="si"
while elec0002=="si" or elec0002=="sí":
    print("Espero estés teniendo un excelente día.\n")
    print("¿Qué deseas hacer?\n")
    election01=str(input("1) CIDR a decimal punteado.\n2) De bits a números.\n3) División de redes.\n4) De números a bits.\n5) Ayuda.\n6) Salir.\n\n"))
    cls()
    if election01=="1":
        DeBitsDeRed()
        elec0002=input("¿Quieres seleccionar otra opción? si/no: ")
        print("")
        if elec0002=="si" or elec0002=="sí":
            cls()
    elif election01=="2":
        BitsToNum()
        elec0002=input("¿Quieres seleccionar otra opción? si/no: ")
        print("")
        if elec0002=="si" or elec0002=="sí":
            cls()        
    elif election01=="3":
        print("Hola buenos días.\n")
        division_redes()
        elec0002=input("¿Quieres seleccionar otra opción? si/no: ")
        print("")
        if elec0002=="si" or elec0002=="sí":
            cls()
    elif election01=="4":
        NumToBits()
        elec0002=input("¿Quieres seleccionar otra opción? si/no: ")
        print("")
        if elec0002=="si" or elec0002=="sí":
            cls()
    elif election01=="5":
        print("\n1) Puede traducir la máscara CIDR a decimal punteado.\n2) Puede traducir de binario a decimal, no hay límite de bits. \n3) Puede hacer divisiones de red, entrega multiples valores.\n4) Puede traducir números decimales a binario, no hay límite en el tamaño de los números. \n \nTen cuidado al introducir valores no señalados o espacios en blanco.")
        election01=str(input())
        cls()
    elif election01=="6":
        print("Fin del código.")
        time.sleep(3)
        exit()
    else:
        print("Fuera de rango.")
        elec0002=input("¿Quieres seleccionar otra opción? si/no: ")
        print("")
        if elec0002=="si" or elec0002=="sí":
            cls()
print("Fin del código.")
time.sleep(3)