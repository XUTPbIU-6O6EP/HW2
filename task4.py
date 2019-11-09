print ('Введите субсидии и количество голов скота')
subsidii=int(input())
golovi=int(input())
for b in range (1, subsidii//20):
    k=-golovi-3*b+subsidii/5
    t=golovi-b-k
    print (b, int(k), int(t))
    if k<=0:
        break;
