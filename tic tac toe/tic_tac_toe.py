M = [['-','-','-'],['-','-','-'],['-','-','-']]
br = 0
w = 0
def ispis(M):
    for i in range(len(M)):
        for j in (M[i]):
            print(j,' ',end='')
        print()
def pobjednik(M):
    global w
    if M[0][0] == M[0][1] == M[0][2] != '-':
        print(M[0][0],' je pobjedio! Čestitamo!')
        print('Za ponovnu igru unesite riječ ponovno .')
        print('Ako ste završili s igrom unesite riječ kraj.')
        w += 1
        return False
    elif M[1][0] == M[1][1] == M[1][2] != '-':
        print(M[1][0],' je pobjedio! Čestitamo!')
        print('Za ponovnu igru unesite riječ ponovno .')
        print('Ako ste završili s igrom unesite riječ kraj.')
        w += 1
        return False
    elif M[2][0] == M[2][1] == M[2][2] != '-':
        print(M[2][0],' je pobjedio! Čestitamo!')
        print('Za ponovnu igru unesite riječ ponovno .')
        print('Ako ste završili s igrom unesite riječ kraj.')
        w += 1
        return False
    elif M[0][0] == M[1][0] == M[2][0] != '-':
        print(M[0][0],' je pobjedio! Čestitamo!')
        print('Za ponovnu igru unesite riječ ponovno .')
        print('Ako ste završili s igrom unesite riječ kraj.')
        w += 1
        return False
    elif M[0][1] == M[1][1] == M[2][1] != '-':
        print(M[0][1],' je pobjedio! Čestitamo!')
        print('Za ponovnu igru unesite riječ ponovno .')
        print('Ako ste završili s igrom unesite riječ kraj.')
        w += 1
        return False
    elif M[0][2] == M[1][2] == M[2][2] != '-':
        print(M[0][2],' je pobjedio! Čestitamo!')
        print('Za ponovnu igru unesite riječ ponovno .')
        print('Ako ste završili s igrom unesite riječ kraj.')
        w += 1
        return False
    elif M[0][0] == M[1][1] == M[2][2] != '-':
        print(M[0][0],' je pobjedio! Čestitamo!')
        print('Za ponovnu igru unesite riječ ponovno .')
        print('Ako ste završili s igrom unesite riječ kraj.')
        w += 1
        return False
    elif M[0][2] == M[1][1] == M[2][0] != '-':
        print(M[0][2],' je pobjedio! Čestitamo!')
        print('Za ponovnu igru unesite riječ ponovno .')
        print('Ako ste završili s igrom unesite riječ kraj.')
        w += 1
        return False
def replace(x):
    global br
    M1 =[1,2,3,4,5,6,7,8,9]
    M2 =['2,0','2,1','2,2','1,0','1,1','1,2','0,0','0,1','0,2']
    L = M2[M1.index(x)].split(',')
    if M[eval(L[0])][eval(L[1])]=='-':
        M[eval(L[0])][eval(L[1])]='x'
    else:
        print('Hej,hej! To mjesto je zauzeto! Gubiš svoj potez!')
    br += 1
    if br == 9:
        ispis(M)
        return False
def zamjeni(x):
    global br
    M1 =[1,2,3,4,5,6,7,8,9]
    M2 =['2,0','2,1','2,2','1,0','1,1','1,2','0,0','0,1','0,2']
    L = M2[M1.index(x)].split(',')
    if M[eval(L[0])][eval(L[1])]=='-':
        M[eval(L[0])][eval(L[1])]='o'
    else:
        print('Hej,hej! To mjesto je zauzeto! Gubiš svoj potez!')
    br += 1
    if br == 9:
        ispis(M)
        return False
def igra():
    ispis(M)
    print('Dobro došli u igru križić-kružić!')
    print('Mreža gore prestavlja prazno polje za igru. Prvi je na redu igrač x.')
    print('Mreža brojeva na tipkovnici predstavlja mrežu igre(npr. odaberite broj 5 za polje u sredini).')
    print('Ako probaš odabrati mjesto koje je već zauzeto gubiš svoj potez!')
    print('Uživajte u igri :)')
    global br
    global w
    while  br != 9:

        x = (int(input()))
        
        if replace(x) ==False:
            break
        ispis(M)
        if pobjednik(M) == False:
            break
        print('Sljedeći na redu je igrač o ! ')
        
        o = (int(input()))
          
        if zamjeni(o) == False:
            break
        ispis(M)
        if pobjednik(M) == False:
            break    
        print('Sljedeći na redu je igrač x ! ')

igra()
if w == 0:
    print('Rezultat je izjednačen! Za ponovni pokušaj unesite riječ ponovno .')
    print('Ako ste završili s igrom unesite riječ kraj.')
p = input()
if p == 'ponovno':
    M = [['-','-','-'],['-','-','-'],['-','-','-']]
    br = 0 
    igra()
elif p == 'kraj':
    print('Nadamo se da ste uživali u igri :)')
