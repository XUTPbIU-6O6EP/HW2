print ('Vvedite kol-vo dnej')
N=int(input())
sr1=[]
for i in range (0,N,1):
    t1=[]
    print('Vvedite kol-vo zabegov')
    Z=int(input())
    for i in range (0,Z,1):
        print('Vvedite T & S=')
        t=input()
        t=t.split()
        t1.append(int(t[1])/int(t[0]))
    sr1.append(sum(t1))
sr1.sort(reverse=True)
for i in range (len(sr1)):
    print (round(sr1[i],4))
