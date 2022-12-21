from tkinter import *
from tkinter import messagebox
from playsound import playsound

root = Tk()
root.config(bg='light yellow')
root.resizable(False, False)

root.geometry('800x650')

global lista_polja
lista_polja = [['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', '']]

listabrodovi_player1 = [['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '']]

listabrodovi_player1_labeli = [['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', '']]

listabrodovi_player2 = [['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '']]

listabrodovi_player2_labeli = [['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', ''],
                               ['', '', '', '', '', '', '', '', '', '']]

global brojac_za_playere
brojac_za_playere = 0
global lista_za_sejvanje_labela
global lista_za_sejvanje_brodova
lista_za_sejvanje_labela = listabrodovi_player1_labeli
lista_za_sejvanje_brodova = listabrodovi_player1


def show_grid():
    global player_label
    player_label = Label(root, bg='light yellow', text='Player 1', font='Fixedsys 25')
    player_label.place(relx=0.508, rely=0.059, width=200, height=50, anchor='center')
    if brojac_za_playere == 5:
        player_label.config(text='Player 2')
    pomakx = 0.18
    pomaky = 0.14

    for i in range(10):
        for y in range(10):
            lista_polja[i][y] = Label(root, bg='blue', borderwidth=5)
            lista_polja[i][y].place(relx=pomakx, rely=pomaky, height=50, width=50)
            pomakx += 0.065
        pomakx = 0.18
        pomaky += 0.08

    postavljanje_brodova_sa_strane()


global broj_3_brodova
broj_3_brodova = 0

global rotacija
rotacija = 'vodoravno'


def rotiranje(event):
    global rotacija
    if rotacija == 'vodoravno':
        rotacija = 'vertikalno'
    else:
        rotacija = 'vodoravno'


def rotacija_2(i, y):
    global rotacija
    change(1, i, y)
    if rotacija == 'vodoravno':
        rotacija = 'vertikalno'
    else:
        rotacija = 'vodoravno'
    change(0, i, y)


def save_pozicije(lista_pozicija, n, i, y, radnja):
    global broj_3_brodova

    if rotacija == 'vodoravno':
        if radnja == 'stavljanje':
            if n == 3:
                if broj_3_brodova < 3:
                    for z in range(0, n):
                        lista_pozicija[i][y + z] = 'b' + str(n) + '.1'
                        broj_3_brodova += 1
                else:
                    for z in range(0, n):
                        lista_pozicija[i][y + z] = 'b' + str(n) + '.2'

            else:
                for z in range(0, n):
                    lista_pozicija[i][y + z] = 'b' + str(n)
        for br in range(0, n):
            if br == 0:
                if (i - 1 >= 0):
                    lista_pozicija[i - 1][y] = provjera_xeva(lista_pozicija[i - 1][y], radnja)
                    if (y - 1 >= 0):
                        lista_pozicija[i - 1][y - 1] = provjera_xeva(lista_pozicija[i - 1][y - 1], radnja)
                if (y - 1 >= 0):
                    lista_pozicija[i][y - 1] = provjera_xeva(lista_pozicija[i][y - 1], radnja)
                if i + 1 <= 9:
                    lista_pozicija[i + 1][y] = provjera_xeva(lista_pozicija[i + 1][y], radnja)
                    if y - 1 >= 0:
                        lista_pozicija[i + 1][y - 1] = provjera_xeva(lista_pozicija[i + 1][y - 1], radnja)
                y += 1
            elif br == n - 1:
                if i - 1 >= 0:
                    lista_pozicija[i - 1][y] = provjera_xeva(lista_pozicija[i - 1][y], radnja)
                    if y + 1 <= 9:
                        lista_pozicija[i - 1][y + 1] = provjera_xeva(lista_pozicija[i - 1][y + 1], radnja)
                if y + 1 <= 9:
                    lista_pozicija[i][y + 1] = provjera_xeva(lista_pozicija[i][y + 1], radnja)
                if i + 1 <= 9:
                    lista_pozicija[i + 1][y] = provjera_xeva(lista_pozicija[i + 1][y], radnja)
                    if y + 1 <= 9:
                        lista_pozicija[i + 1][y + 1] = provjera_xeva(lista_pozicija[i + 1][y + 1], radnja)
                y += 1
            else:
                if i - 1 >= 0:
                    lista_pozicija[i - 1][y] = provjera_xeva(lista_pozicija[i - 1][y], radnja)
                if i + 1 <= 9:
                    lista_pozicija[i + 1][y] = provjera_xeva(lista_pozicija[i + 1][y], radnja)
                y += 1

    if rotacija == 'vertikalno':
        if radnja == 'stavljanje':
            if n == 3:
                if broj_3_brodova < 3:
                    for z in range(0, n):
                        lista_pozicija[i + z][y] = 'b' + str(n) + '.1'
                        broj_3_brodova += 1
                else:
                    for z in range(0, n):
                        lista_pozicija[i + z][y] = 'b' + str(n) + '.2'

            else:
                for z in range(0, n):
                    lista_pozicija[i + z][y] = 'b' + str(n)
        for br in range(0, n):
            if br == 0:
                if y - 1 >= 0:
                    lista_pozicija[i][y - 1] = provjera_xeva(lista_pozicija[i][y - 1], radnja)
                if i - 1 >= 0:
                    lista_pozicija[i - 1][y] = provjera_xeva(lista_pozicija[i - 1][y], radnja)
                    if y - 1 >= 0:
                        lista_pozicija[i - 1][y - 1] = provjera_xeva(lista_pozicija[i - 1][y - 1], radnja)
                    if y + 1 <= 9:
                        lista_pozicija[i - 1][y + 1] = provjera_xeva(lista_pozicija[i - 1][y + 1], radnja)
                if y + 1 <= 9:
                    lista_pozicija[i][y + 1] = provjera_xeva(lista_pozicija[i][y + 1], radnja)
                i += 1
            elif br == n - 1:
                if i + 1 <= 9:
                    lista_pozicija[i + 1][y] = provjera_xeva(lista_pozicija[i + 1][y], radnja)
                    if y + 1 <= 9:
                        lista_pozicija[i + 1][y + 1] = provjera_xeva(lista_pozicija[i + 1][y + 1], radnja)
                    if y - 1 >= 0:
                        lista_pozicija[i + 1][y - 1] = provjera_xeva(lista_pozicija[i + 1][y - 1], radnja)
                if y + 1 <= 9:
                    lista_pozicija[i][y + 1] = provjera_xeva(lista_pozicija[i][y + 1], radnja)
                if y - 1 >= 0:
                    lista_pozicija[i][y - 1] = provjera_xeva(lista_pozicija[i][y - 1], radnja)
                i += 1
            else:
                if y - 1 >= 0:
                    lista_pozicija[i][y - 1] = provjera_xeva(lista_pozicija[i][y - 1], radnja)
                if y + 1 <= 9:
                    lista_pozicija[i][y + 1] = provjera_xeva(lista_pozicija[i][y + 1], radnja)
                i += 1

    for z in lista_pozicija:
        print(z)


def provjera_xeva(stvar_za_provjeru, koja_provjera):
    if stvar_za_provjeru == 'x':
        if koja_provjera == 'stavljanje':
            return 'x2'
        elif koja_provjera == 'micanje':
            return ''
    elif stvar_za_provjeru == 'x2':
        if koja_provjera == 'stavljanje':
            return 'x3'
        elif koja_provjera == 'micanje':
            return 'x'
    elif stvar_za_provjeru == 'x3':
        if koja_provjera == 'stavljanje':
            return 'x4'
        elif koja_provjera == 'micanje':
            return 'x2'
    elif stvar_za_provjeru == 'x4':
        return 'x3'
    else:
        if koja_provjera == 'stavljanje':
            return 'x'
        elif koja_provjera == 'micanje':
            return ''


def promjena_boje_jedankod(š, brodz):
    global n
    n = š
    global brod
    global broj_3_brodova
    brod = brodz
    global lista_za_sejvanje_labela
    global lista_za_sejvanje_brodova
    global rotacija
    if brojac_za_playere == 5:
        lista_za_sejvanje_labela = listabrodovi_player2_labeli
        lista_za_sejvanje_brodova = listabrodovi_player2
        broj_3_brodova = 0

    for i in range(10):
        for y in range(10):
            lista_polja[i][y].bind('<Enter>', lambda event, z=i, p=y: change(0, z, p))
            lista_polja[i][y].bind('<Leave>', lambda event, z=i, p=y: change(1, z, p))
            lista_polja[i][y].bind('<Button-1>', lambda event, z=i, p=y: promjeniusivu(n, z, p))
            lista_polja[i][y].bind('<Button-3>', lambda event, z=i, p=y: rotacija_2(z, p))


def change(kojaradnja, i, y):
    if rotacija == 'vodoravno':
        dozvola = True
        for q in range(11 - n, 10):
            if y == q:
                dozvola = False

        if dozvola:
            for q in range(0, n):
                if lista_za_sejvanje_brodova[i][y + q] != '':
                    dozvola = False

        if dozvola:
            for z in range(0, n):
                if kojaradnja == 0:
                    lista_polja[i][y + z].config(bg='light blue')
                elif kojaradnja == 1:
                    lista_polja[i][y + z].config(bg='blue')
        else:
            for q in range(11 - n, 10):
                if y == q:
                    for z in range(0, 10 - q):
                        if kojaradnja == 0:
                            lista_polja[i][y + z].config(bg='red')
                        elif kojaradnja == 1:
                            lista_polja[i][y + z].config(bg='blue')

            for p in range(0, n):
                if (y + p) <= 9:
                    if kojaradnja == 0:
                        lista_polja[i][y + p].config(bg='red')
                    elif kojaradnja == 1:
                        lista_polja[i][y + p].config(bg='blue')
    elif rotacija == 'vertikalno':
        dozvola = True
        for q in range(11 - n, 10):
            if i == q:
                dozvola = False

        if dozvola:
            for q in range(0, n):
                if lista_za_sejvanje_brodova[i + q][y] != '':
                    dozvola = False

        if dozvola:
            for z in range(0, n):
                if kojaradnja == 0:
                    lista_polja[i + z][y].config(bg='light blue')
                elif kojaradnja == 1:
                    lista_polja[i + z][y].config(bg='blue')
        else:
            for q in range(11 - n, 10):
                if i == q:
                    for z in range(0, 10 - q):
                        if kojaradnja == 0:
                            lista_polja[i + z][y].config(bg='red')
                        elif kojaradnja == 1:
                            lista_polja[i + z][y].config(bg='blue')

            for p in range(0, n):
                if (i + p) <= 9:
                    if kojaradnja == 0:
                        lista_polja[i + p][y].config(bg='red')
                    elif kojaradnja == 1:
                        lista_polja[i + p][y].config(bg='blue')


def promjeniusivu(n, i, y):
    global brojac_za_playere
    dozvola = True
    global ship_placed
    ship_placed = False

    if rotacija == 'vodoravno':
        for q in range(11 - n, 10):
            if y == q:
                dozvola = False
        if dozvola:
            for q in range(y, y + n):
                if lista_za_sejvanje_brodova[i][q] != '':
                    dozvola = False

        if dozvola:
            for z in range(0, n):
                lista_za_sejvanje_labela[i][y + z] = Label(root, bg='gray', borderwidth=5)
                lista_za_sejvanje_labela[i][y + z].place(relx=0.065 * (y + z) + 0.18, rely=0.08 * i + 0.14,
                                                         height=50,
                                                         width=50)

                lista_za_sejvanje_labela[i][y + z].bind('<Button-1>',
                                                        lambda event, p=i, o=y, koji_brod=brod:
                                                        pickup(n, p, o, 'vodoravno', koji_brod))
            print(brod)
            ship_placed = True
            save_pozicije(lista_za_sejvanje_brodova, n, i, y, 'stavljanje')
        else:
            messagebox.showwarning('Warning', 'Nemoguće postaviti brod na odabranu poziciju.')
    if rotacija == 'vertikalno':
        for q in range(11 - n, 10):
            if i == q:
                dozvola = False

        if dozvola:
            for q in range(i, i + n):
                if lista_za_sejvanje_brodova[q][y] != '':
                    dozvola = False

        if dozvola:
            for z in range(0, n):
                lista_za_sejvanje_labela[i + z][y] = Label(root, bg='gray', borderwidth=5)
                lista_za_sejvanje_labela[i + z][y].place(relx=0.065 * y + 0.18, rely=0.08 * (i + z) + 0.14,
                                                         height=50,
                                                         width=50)

                lista_za_sejvanje_labela[i + z][y].bind('<Button-1>',
                                                        lambda event, p=i, o=y, koji_brod=brod:
                                                        pickup(n, p, o, 'vertikalno', koji_brod))

            ship_placed = True
            save_pozicije(lista_za_sejvanje_brodova, n, i, y, 'stavljanje')
        else:
            messagebox.showwarning('Warning', 'Nemoguće postaviti brod na odabranu poziciju.')

    if ship_placed:
        for q in range(10):
            for z in range(10):
                lista_polja[q][z].bind('<Enter>', nista)
                lista_polja[q][z].bind('<Leave>', nista)
                lista_polja[q][z].bind('<Button-1>', nista)
                lista_polja[q][z].bind('<Button-3>', nista)
                brod.config(bg='light grey')
                brod.bind('<Button-1>', nista)
        brojac_za_playere += 1
        if brojac_za_playere == 5:
            global im_done
            im_done = Button(root, bg='grey', text='Press if u happi')
            im_done.place(relx=0.7, rely=0.05, width=100, height=50)
            im_done.bind('<Button-1>', sljedeci_igrac)

        elif brojac_za_playere == 10:
            global pokreni_drugu_fazu
            pokreni_drugu_fazu = Button(root, bg='grey', text='Press if u happi')
            pokreni_drugu_fazu.place(relx=0.7, rely=0.05, width=100, height=50)
            pokreni_drugu_fazu.bind('<Button-1>', faza_pucanja)


def pickup(n, i, y, rotacija_polozenog_broda, brodz):
    dopuštenje = True
    global broj_3_brodova
    print(brodz)
    global brojac_za_playere
    global rotacija
    rotacija = rotacija_polozenog_broda
    if brojac_za_playere == 5:
        im_done.destroy()
    elif brojac_za_playere == 10:
        pokreni_drugu_fazu.destroy()
    brojac_za_playere += -1
    brodz.config(bg='grey')
    brodz.bind('<Button-1>', lambda event: promjena_boje_jedankod(n, brodz))
    brodz.bind('<Button-3>', rotiranje)
    if rotacija_polozenog_broda == 'vertikalno':
        for z in range(0, n):
            lista_za_sejvanje_labela[i + z][y].destroy()
            lista_za_sejvanje_labela[i + z][y] = ''
            lista_za_sejvanje_brodova[i + z][y] = ''
            lista_polja[i + z][y].config(bg='blue')
    elif rotacija_polozenog_broda == 'vodoravno':
        for z in range(0, n):
            lista_za_sejvanje_labela[i][y + z].destroy()
            lista_za_sejvanje_labela[i][y + z] = ''
            lista_za_sejvanje_brodova[i][y + z] = ''
            lista_polja[i][y + z].config(bg='blue')
    if n == 3:
        for u in lista_za_sejvanje_brodova:
            if 'b3.1' in u:
                dopuštenje = False

        if dopuštenje:
            broj_3_brodova = 0

    save_pozicije(lista_za_sejvanje_brodova, n, i, y, 'micanje')
    promjena_boje_jedankod(n, brodz)
    print('')


def postavljanje_brodova_sa_strane():
    brod2 = Label(root, bg='grey', borderwidth=10, highlightbackground='red')
    brod2.place(relx=0.88, rely=0.14, height=100, width=50)
    brod2.bind('<Button-1>', lambda event: promjena_boje_jedankod(2, brod2))
    brod2.bind('<Button-3>', rotiranje)
    brod3_1 = Label(root, bg='grey')
    brod3_1.place(relx=0.07, rely=0.18, height=150, width=50)
    brod3_1.bind('<Button-1>', lambda event: promjena_boje_jedankod(3, brod3_1))
    brod3_1.bind('<Button-3>', rotiranje)
    brod3_2 = Label(root, bg='grey')
    brod3_2.place(relx=0.88, rely=0.707, height=150, width=50)
    brod3_2.bind('<Button-1>', lambda event: promjena_boje_jedankod(3, brod3_2))
    brod3_2.bind('<Button-3>', rotiranje)
    brod4 = Label(root, bg='grey')
    brod4.place(relx=0.88, rely=0.347, height=200, width=50)
    brod4.bind('<Button-1>', lambda event: promjena_boje_jedankod(4, brod4))
    brod4.bind('<Button-3>', rotiranje)
    brod5 = Label(root, bg='grey')
    brod5.place(relx=0.07, rely=0.52, height=250, width=50)
    brod5.bind('<Button-1>', lambda event: promjena_boje_jedankod(5, brod5))
    brod5.bind('<Button-3>', rotiranje)


def nista(event):
    return


def nista2():
    return


def sljedeci_igrac(event):
    clear()
    show_grid()
    im_done.destroy()


def clear():
    L = root.place_slaves()
    for i in range(len(L)):
        L[i].destroy()


global broj_pucanja
broj_pucanja = 0


def faza_pucanja(event):
    clear()
    pomakx = 0.18
    pomaky = 0.14

    global label_playera
    label_playera = Label(root, bg='light yellow', text='Player 1', font='Fixedsys 25')
    label_playera.place(relx=0.508, rely=0.059, width=200, height=50, anchor='center')
    global label_upozorenja
    label_upozorenja = Label(root, bg='light yellow', font='Fixedsys 20', fg='red')
    label_upozorenja.place(relx=0.5, rely=0.12, anchor='center')

    for i in range(10):
        for y in range(10):
            listabrodovi_player1_labeli[i][y] = Label(root, bg='blue', borderwidth=5)
            listabrodovi_player2_labeli[i][y] = Label(root, bg='blue', borderwidth=5)
            listabrodovi_player1_labeli[i][y].place(relx=pomakx, rely=pomaky, height=50, width=50)
            listabrodovi_player1_labeli[i][y].bind('<Button-1>', lambda event, n='lijevi', z=i, p=y: potez(n, z, p))
            listabrodovi_player1_labeli[i][y].bind('<Button-3>', lambda event, n='desni', z=i, p=y: potez(n, z, p))
            listabrodovi_player2_labeli[i][y].bind('<Button-1>', lambda event, n='lijevi', z=i, p=y: potez(n, z, p))
            listabrodovi_player2_labeli[i][y].bind('<Button-3>', lambda event, n='desni', z=i, p=y: potez(n, z, p))
            pomakx += 0.065
        pomakx = 0.18
        pomaky += 0.08

    global player_na_redu
    player_na_redu = 'Prvi'

    def potez(koji, i, y):
        global player_na_redu

        def puc_puc(i, y):

            global player_na_redu
            global broj_pucanja

            broj_pucanja += 1

            if broj_pucanja == 1:
                if player_na_redu == 'Prvi':

                    if 'b' in listabrodovi_player2[i][y]:
                        broj_pucanja = 0
                        br = 0
                        brp = 0
                        a = listabrodovi_player2[i][y]
                        listabrodovi_player1_labeli[i][y].place_forget()
                        listabrodovi_player1_labeli[i][y] = Label(root, borderwidth=5, bg='red')
                        listabrodovi_player1_labeli[i][y].place(relx=0.065 * y + 0.18, rely=0.08 * i + 0.14, height=50,
                                                                width=50)
                        listabrodovi_player2[i][y] = 'p'
                        for k in listabrodovi_player2:
                            if a in k:
                                br += 1
                            for n in k:
                                if 'b' in n:
                                    brp += 1
                        if br == 0 and brp > 0:
                            playsound('veliki_boom2.wav', False)
                            messagebox.showinfo('Info', 'Brod ' + a + ' je potopljen!')
                        if brp == 0:
                            messagebox.showinfo('Info', player_na_redu + ' igrač je pobijedio!')
                        if br != 0 and brp != 0:
                            print('POGODAK')
                            playsound('boom4.wav', False)
                    else:
                        listabrodovi_player1_labeli[i][y].place_forget()
                        listabrodovi_player1_labeli[i][y] = Label(root, borderwidth=5, bg='black')
                        listabrodovi_player1_labeli[i][y].place(relx=0.065 * y + 0.18, rely=0.08 * i + 0.14, height=50,
                                                                width=50)
                        print('MISS')
                elif player_na_redu == 'Drugi':

                    if 'b' in listabrodovi_player1[i][y]:
                        broj_pucanja = 0
                        br = 0
                        brp = 0
                        a = listabrodovi_player1[i][y]
                        listabrodovi_player2_labeli[i][y].place_forget()
                        listabrodovi_player2_labeli[i][y] = Label(root, borderwidth=5, bg='red')
                        listabrodovi_player2_labeli[i][y].place(relx=0.065 * y + 0.18, rely=0.08 * i + 0.14, height=50,
                                                                width=50)
                        listabrodovi_player1[i][y] = 'p'
                        for k in listabrodovi_player1:
                            if a in k:
                                br += 1
                            for n in k:
                                if 'b' in n:
                                    brp += 1
                        if br == 0 and brp > 0:
                            playsound('veliki_boom2.wav', False)
                            messagebox.showinfo('Info', 'Brod ' + a + ' je potopljen!')

                        if brp == 0:
                            messagebox.showinfo('Info', player_na_redu + ' igrač je pobijedio!')
                        if br != 0 and brp != 0:
                            print('POGODAK')
                            playsound('boom4.wav', False)
                    else:
                        listabrodovi_player2_labeli[i][y].place_forget()
                        listabrodovi_player2_labeli[i][y] = Label(root, borderwidth=5, bg='black')
                        listabrodovi_player2_labeli[i][y].place(relx=0.065 * y + 0.18, rely=0.08 * i + 0.14, height=50,
                                                                width=50)
                        print('MISS')
            else:
                label_upozorenja.config(text='Topovi su ti prazni.')
                root.after(4000, lambda: label_upozorenja.config(text=''))

        def nema_broda(i, y):

            global player_na_redu

            if player_na_redu == 'Prvi':
                if (listabrodovi_player1_labeli[i][y].cget('background') == 'grey'):
                    listabrodovi_player1_labeli[i][y].config(bg='blue')
                else:
                    listabrodovi_player1_labeli[i][y].config(bg='grey')
            if player_na_redu == 'Drugi':
                if (listabrodovi_player2_labeli[i][y].cget('background') == 'grey'):
                    listabrodovi_player2_labeli[i][y].config(bg='blue')
                else:
                    listabrodovi_player2_labeli[i][y].config(bg='grey')

        if koji == 'lijevi':
            puc_puc(i, y)
        if koji == 'desni':
            nema_broda(i, y)

    def promjena_playera(event):
        global player_na_redu
        global broj_pucanja

        if broj_pucanja != 0:

            broj_pucanja = 0

            if player_na_redu == 'Prvi':
                player_na_redu = 'Drugi'
            else:
                player_na_redu = 'Prvi'

            if player_na_redu == 'Prvi':
                label_playera.config(text='Player 1')
                pomakx = 0.18
                pomaky = 0.14

                for i in range(10):
                    for y in range(10):
                        listabrodovi_player2_labeli[i][y].place_forget()
                        listabrodovi_player1_labeli[i][y].place(relx=pomakx, rely=pomaky, height=50, width=50)
                        pomakx += 0.065
                    pomakx = 0.18
                    pomaky += 0.08

            if player_na_redu == 'Drugi':
                label_playera.config(text='Player 2')

                pomakx = 0.18
                pomaky = 0.14

                for i in range(10):
                    for y in range(10):
                        listabrodovi_player1_labeli[i][y].place_forget()
                        listabrodovi_player2_labeli[i][y].place(relx=pomakx, rely=pomaky, height=50, width=50)
                        pomakx += 0.065
                    pomakx = 0.18
                    pomaky += 0.08
        else:
            label_upozorenja.config(text='Nisi jos pucao.')
            root.after(4000, lambda: label_upozorenja.config(text=''))

    next_player_button = Button(root, text='next player', font='Fixedsys1 15')
    next_player_button.bind('<Button-1>', promjena_playera)
    next_player_button.place(x=20, y=10, width=100, height=50)


show_grid()

root.mainloop()
