fix_price = 50
delivery = 500
box_vol = 25
babka = 300
s = int(input())    #Стоимость 1 круассана в школе
D = int(input())    #Количество дней
A1=0
B1=0
for i in range (0,D,1):
    A=input()      #кол-во купленных в "Перекрестье", кол-во проданных в школке
    A=A.split()
    A1+=int(A[0])
    B1+=int(A[1])
loss = A1 * fix_price + delivery + babka * round(A1 / box_vol)
viruchka = s * B1
Pribil = viruchka - loss
R = Pribil / viruchka
if R>0.3:
    print ('"Yes"')
else:
    print ('"No"')
