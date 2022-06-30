opcion = 0
class ProdN:
   
    def Binomioalcuadrado (self):
        va1 = input("Escriba el factor 1 -->")
        va2 = float(input("Escriba el factor 2 -->"))
        print (va1, chr(94), 2 ,chr(43), 2*va2,chr(40), va1,chr(41),chr(43),  va2**2 )   
class cdr:
            
    def cuadradodeunaresta (self):
        va1 = input("Escriba el factor 1 -->")
        va2 = float(input("Escriba el factor 2 -->"))
        print (va1, chr(94), 2 ,chr(45), 2*va2,chr(40), va1,chr(41),chr(43),  va2**2 ) 
class difbin:
        
    def Resultadodediferenciaentrebinomios (self):
        va1 = input("Escriba el factor 1 -->")
        va2 = input("Escriba el factor 2 -->")
        print (va1, chr(94), 2 ,chr(45) , va2, chr(94), 2) 
class cubsum:
                
    def cubodeunasuma (self):
        va1 = input("Escriba el factor 1 -->")
        va2 = input("Escriba el factor 2 -->")
        print (va1,chr(94),3,chr(43), 3, chr(40), va1, chr(41) ,chr(94), 2, chr(40), va2,chr(41), chr(43), 3, chr(40), va1, chr(41),  chr(40), va2,chr(41),chr(94), 2, chr(43), va2 ,chr(94),2)           
class cubres:

    def cubodeunaresta (self):
        va1 = input("Escriba el factor 1 -->")
        va2 = input("Escriba el factor 2 -->")
        print(va1,chr(94),3,chr(45), 3, chr(40), va1, chr(41) ,chr(94), 2, chr(40), va2,chr(41), chr(43), 3, chr(40), va1, chr(41),  chr(40), va2,chr(41),chr(94), 2, chr(45), va2 ,chr(94),2)           
class probin:

    def Productodedosbinomios ():
        va1 = input("Escriba el factor 1, 3 -->")
        va2 = input("Escriba el factor 2 -->")
        va4 = input("Escriba el factor 4 -->")
        print (va1,chr(94),2, chr(43),chr(40), va1,chr(41),chr(40), va2,chr(43), va1 ,chr(41),chr(43),chr(40), va2,chr(41),chr(40), va4,chr(41))            
class fin:

    def Finalizarelprograma ():
        print ("gracias, hasta pronto")
        quit()
opcion = int(input("Seleccione la operacion a realizar --->"))
if opcion ==1:
    ProdN
    Binomioalcuadrado()
if opcion ==2:
    cdr
if opcion ==3:
    difbin
if opcion ==4:
    cubsum
if opcion ==5:
    cubres
if opcion ==6:
    probin
if opcion ==7:
    fin
