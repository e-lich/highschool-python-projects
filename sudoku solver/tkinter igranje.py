from tkinter import *
import ctypes

user32 = ctypes.windll.user32
sw = int(user32.GetSystemMetrics(0)/2)
sh = int(user32.GetSystemMetrics(1)/2)

window = Tk()
window.title('Sudoku Solver')
window.iconbitmap('sudoku.ico')
window.configure(background='gray')
window.geometry('600x350+'+str(sw-300)+'+'+str(sh-175))


def pack(dic):
    x = 0
    z = 7
    g = 31
    for m in range(3):
        for i in range(3):
            for k in range(3):
                for l in range(3):
                    field.create_window(z + l * 51, g + i * 51, window=dic[x], width=48, height=48, anchor=W)
                    x += 1
                z += 155
            z = 7
        g += 155
    field.pack()


def find(k, a, b, L):
    ime = str(a) + str(b)
    K = [['00', '01', '02', '10', '11', '12', '20', '21', '22'], ['03', '04', '05', '13', '14', '15', '23', '24', '25'],
         ['06', '07', '08', '16', '17', '18', '26', '27', '28'], ['30', '31', '32', '40', '41', '42', '50', '51', '52'],
         ['33', '34', '35', '43', '44', '45', '53', '54', '55'], ['36', '37', '38', '46', '47', '48', '56', '57', '58'],
         ['60', '61', '62', '70', '71', '72', '80', '81', '82'], ['63', '64', '65', '73', '74', '75', '83', '84', '85'],
         ['66', '67', '68', '76', '77', '78', '86', '87', '88']]
    P = []
    for p in range(9):
        P.append(L[p][b])
    S = []
    if (L[a].count(str(k)) + L[a].count(k)) < 1:
        if (P.count(str(k)) + P.count(k)) < 1:
            for g in K:
                if ime in g:
                    for x in g:
                        if x != ime:
                            S.append(L[int(x[0])][int(x[1])])
                    if str(k) not in S and k not in S:
                        return True
                    else:
                        return False


def check(k, a, b, L):
    ime = str(a) + str(b)
    K = [['00', '01', '02', '10', '11', '12', '20', '21', '22'], ['03', '04', '05', '13', '14', '15', '23', '24', '25'],
         ['06', '07', '08', '16', '17', '18', '26', '27', '28'], ['30', '31', '32', '40', '41', '42', '50', '51', '52'],
         ['33', '34', '35', '43', '44', '45', '53', '54', '55'], ['36', '37', '38', '46', '47', '48', '56', '57', '58'],
         ['60', '61', '62', '70', '71', '72', '80', '81', '82'], ['63', '64', '65', '73', '74', '75', '83', '84', '85'],
         ['66', '67', '68', '76', '77', '78', '86', '87', '88']]
    P = []
    for p in range(9):
        P.append(L[p][b])
    S = []
    if L[a].count(k) == 1:
        if P.count(k) == 1:
            for g in K:
                if ime in g:
                    for x in g:
                        if x != ime:
                            S.append(L[int(x[0])][int(x[1])])
                    if S.count(k) == 0:
                        return True
                    else:
                        return False


def is_solvable(L):
    for i in L:
        a = L.index(i)
        b = 0
        for j in i:
            if j != '':
                if not check(j, a, b, L):
                    return False
            b += 1
    return True


def is_solved(L):
    z = 0
    for i in L:
        for j in i:
            if j == '':
                z += 1
    if z == 0:
        return True
    else:
        return False


dic_solved = {}

x = 0

def solve(L):
    global x

    if is_solved(L) and x == 0:
        if is_solvable(L):
            x += 1
            prozor_2 = Toplevel()
            prozor_2.title('Info!')
            prozor_2.iconbitmap('sudoku.ico')
            prozor_2.configure(background='gray')
            prozor_2.geometry('700x100+' + str(sw - 350) + '+' + str(sh - 100))

            label_ne = Label(prozor_2, text='This sudoku puzzle is already solved!',
                             font=('Gang of Three', 18), justify='center', fg='brown', bg='gray')
            label_ne.pack()
            button_ok = Button(prozor_2, text='Ok', font=('Gang of Three', 16), command=prozor_2.destroy, bg='gray',
                               fg='brown')
            button_ok.bind('<Button-1>', lambda event: restart(dic))
            button_ok.pack()
            prozor_2.mainloop()
        if not is_solvable(L):
            x += 1
            prozor_2 = Toplevel()
            prozor_2.title('Info!')
            prozor_2.iconbitmap('sudoku.ico')
            prozor_2.configure(background='gray')
            prozor_2.geometry('700x100+' + str(sw - 350) + '+' + str(sh - 100))

            label_ne = Label(prozor_2, text='This sudoku puzzle is already filled out, incorrectly :(',
                             font=('Gang of Three', 18), justify='center', fg='brown', bg='gray')
            label_ne.pack()
            button_ok = Button(prozor_2, text='Ok', font=('Gang of Three', 16), command=prozor_2.destroy, bg='gray',
                               fg='brown')
            button_ok.bind('<Button-1>', lambda event: restart(dic))
            button_ok.pack()
            prozor_2.mainloop()
    if not is_solvable(L) and x == 0:
        x += 1
        prozor_2 = Toplevel()
        prozor_2.title('Info!')
        prozor_2.iconbitmap('sudoku.ico')
        prozor_2.configure(background='gray')
        prozor_2.geometry('700x100+' + str(sw - 350) + '+' + str(sh - 100))

        label_ne = Label(prozor_2, text='This sudoku puzzle is unfortunately not solvable!',
                         font=('Gang of Three', 18), justify='center', fg='brown', bg='gray')
        label_ne.pack()
        button_ok = Button(prozor_2, text='Ok', font=('Gang of Three', 16), command=prozor_2.destroy, bg='gray',
                           fg='brown')
        button_ok.bind('<Button-1>', lambda event: restart(dic))
        button_ok.pack()
        prozor_2.mainloop()
    for i in L:
        for j in i:
            if j.isalpha() and x == 0:
                x += 1
                prozor_2 = Toplevel()
                prozor_2.title('Info!')
                prozor_2.iconbitmap('sudoku.ico')
                prozor_2.configure(background='gray')
                prozor_2.geometry('500x100+' + str(sw - 250) + '+' + str(sh - 100))

                label_ne = Label(prozor_2, text="You can't enter letters stoopid!", font=('Gang of Three', 18),
                                 justify='center',
                                 bg='gray', fg='brown')
                label_ne.pack()
                button_ok = Button(prozor_2, text='Ok', font=('Gang of Three', 16), command=prozor_2.destroy,
                                   bg='gray',
                                   fg='brown')
                button_ok.bind('<Button-1>', lambda event: restart(dic))
                button_ok.pack()
                prozor_2.mainloop()
    for i in L:
        for j in i:
            if j not in ['', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and x == 0:
                x += 1
                prozor_2 = Toplevel()
                prozor_2.title('Info!')
                prozor_2.iconbitmap('sudoku.ico')
                prozor_2.configure(background='gray')
                prozor_2.geometry('600x100+' + str(sw - 300) + '+' + str(sh - 100))

                label_ne = Label(prozor_2, text='The numbers you enter must be from 1 to 9!',
                                 font=('Gang of Three', 18),
                                 justify='center', bg='gray', fg='brown')
                label_ne.pack()
                button_ok = Button(prozor_2, text='Ok', font=('Gang of Three', 16), command=prozor_2.destroy, bg='gray',
                                   fg='brown')
                button_ok.bind('<Button-1>', lambda event: restart(dic))
                button_ok.pack()
                prozor_2.mainloop()
    a = 0
    while not is_solved(L):
        b = 0
        while b != 9:
            y = 0
            if L[a][b] == '':
                for k in range(1, 10):
                    if find(k, a, b, L):
                        L[a][b] = k
                        break
                    else:
                        y += 1
                while y == 9:
                    if b != 0:
                        if not isinstance(L[a][b-1], str):
                            y = L[a][b-1]
                            if y != 9:
                                for o in range(1, (10-L[a][b-1])):
                                    if find((L[a][b-1] + o), a, b-1, L):
                                        L[a][b-1] += o
                                        b -= 1
                                        break
                                    else:
                                        y += 1
                            if y == 9:
                                L[a][b-1] = ''
                                b -= 1
                        else:
                            b -= 1
                    elif a != 0:
                        a -= 1
                        b = 9
                    elif x == 0:
                        x += 1
                        prozor_2 = Toplevel()
                        prozor_2.title('Info!')
                        prozor_2.iconbitmap('sudoku.ico')
                        prozor_2.configure(background='gray')
                        prozor_2.geometry('700x100+' + str(sw - 350) + '+' + str(sh - 100))

                        label_ne = Label(prozor_2, text='This sudoku puzzle is unfortunately not solvable!',
                                         font=('Gang of Three', 18), justify='center', fg='brown', bg='gray')
                        label_ne.pack()
                        button_ok = Button(prozor_2, text='Ok', font=('Gang of Three', 16),
                                           command=prozor_2.destroy, bg='gray',
                                           fg='brown')
                        button_ok.bind('<Button-1>', lambda event: restart(dic))
                        button_ok.pack()
                        prozor_2.mainloop()
            b += 1
        a += 1
    h = 0
    if x == 0:
        for g in L:
            for n in g:
                if isinstance(n, str):
                    dic_solved[h] = Label(field, text=n, font=('Gang of Three', 18, 'bold'), justify='center', bg='gray',
                                          fg='brown4')
                else:
                    dic_solved[h] = Label(field, text=str(n), font=('Gang of Three', 18), justify='center', bg='gray',
                                          fg='coral4')
                h += 1
        pack(dic_solved)


def restart(dictionary, event = None):
    global x
    x = 0
    for i in range(81):
        dic[i] = Entry(field, font=('Gang of Three', 18, 'bold'), justify='center', bg='gray', fg='brown4')

    pack(dic)


def fetching_entries_and_solve(event):
    global dic
    global x

    L = []
    br = 0
    for i in range(9):
        M = []
        for j in range(9):
            M.append(dic[br].get())
            br += 1
        L.append(M)
    solve(L)


def pack_field(event):
    global dic
    global field
    global solve_button
    global restart_button
    global back_button

    window.geometry('700x600' + '+' + str(sw - 350) + '+' + str(sh - 300))

    field_frame = Frame(window, bg='gray')
    field = Canvas(field_frame, width=472, height=472, bg='gray14')

    thin_line_1 = field.create_line(55, 4, 55, 471, fill='grey')
    thin_line_2 = field.create_line(106, 4, 106, 471, fill='grey')
    thin_line_3 = field.create_line(210, 4, 210, 471, fill='grey')
    thin_line_4 = field.create_line(261, 4, 261, 471, fill='grey')
    thin_line_5 = field.create_line(365, 4, 365, 471, fill='grey')
    thin_line_6 = field.create_line(416, 4, 416, 471, fill='grey')

    thin_line_7 = field.create_line(4, 55, 471, 55, fill='grey')
    thin_line_8 = field.create_line(4, 106, 471, 106, fill='grey')
    thin_line_9 = field.create_line(4, 210, 471, 210, fill='grey')
    thin_line_10 = field.create_line(4, 261, 471, 261, fill='grey')
    thin_line_11 = field.create_line(4, 365, 471, 365, fill='grey')
    thin_line_12 = field.create_line(4, 416, 471, 416, fill='grey')

    line_1 = field.create_line(4, 4, 4, 471, width=3)
    line_2 = field.create_line(159, 4, 159, 471, width=3)
    line_3 = field.create_line(314, 4, 314, 471, width=3)
    line_4 = field.create_line(469, 4, 469, 471, width=3)
    line_5 = field.create_line(4, 4, 471, 4, width=3)
    line_6 = field.create_line(4, 159, 471, 159, width=3)
    line_7 = field.create_line(4, 314, 471, 314, width=3)
    line_8 = field.create_line(4, 469, 471, 469, width=3)

    dic = {}

    for i in range(81):
        dic[i] = Entry(field, font=('Gang of Three', 18, 'bold', ), justify='center', bg='gray', fg='brown4')

    frame_home.pack_forget()

    pack(dic)

    solve_button = Button(field_frame, text='Solve', font=('Gang of Three', 18), bg='gray', fg='brown')
    solve_button.bind('<Button-1>', fetching_entries_and_solve)
    solve_button.place(y=476)

    restart_button = Button(field_frame, text='Restart', font=('Gang of Three', 18), bg='gray', fg='brown')
    restart_button.bind('<Button-1>', lambda event: restart(dic))
    restart_button.pack()

    def solve_to_home(event):
        field_frame.pack_forget()
        window.geometry('600x350' + '+' + str(sw - 300) + '+' + str(sh - 175))
        frame_home.pack()

    back_button = Button(field_frame, text='Back', font=('Gang of Three', 18), bg='gray', fg='brown')
    back_button.bind('<Button-1>', solve_to_home)
    back_button.place(x=398, y=476)

    field_frame.pack()


frame_home = Frame(window, bg='gray')

sudoku_png = PhotoImage(file='sudoku.png')
sudoku = Label(master=frame_home, image=sudoku_png)
sudoku.pack()

start_button = Button(frame_home, text="Let's solve!", relief='raised', font=('Gang of Three', 16), bg='gray', fg='brown',
                      width=15)
start_button.bind('<Button-1>', pack_field)
start_button.pack(anchor=N)


def write_instructions(event):
    global sudoku
    global start_button
    global help_button
    global quit_button
    global ins_to_home_button

    window.geometry('1000x350' + '+' + str(sw - 500) + '+' + str(sh - 175))
    frame_home.pack_forget()
    instructions_label = Label(window, text="It's very simple!"+"\n"+"Just enter the numbers you already have,"+"\n" +
                                            "click the 'Solve' button and the rest of the numbers will appear shortly!"
                                            + "\n" + "If you want to restart the field, press 'Restart'. " + "\n" +
                                            "\n" + "Have fun :)",
                               font=('Gang of Three', 20), bg='gray', fg='brown')

    def ins_to_home(event):
        window.geometry('600x350' + '+' + str(sw - 300) + '+' + str(sh - 175))
        ins_to_home_button.pack_forget()
        instructions_label.pack_forget()
        sudoku.pack()
        frame_home.pack()

    ins_to_home_button = Button(window, relief='raised', text="◄", font=('BOLD', 18), bg='gray', fg='brown')
    ins_to_home_button.bind('<Button-1>', ins_to_home)
    ins_to_home_button.pack(anchor=NW)
    instructions_label.pack(fill=BOTH)


help_button = Button(frame_home, text="Help", relief='raised', font=('Gang of Three', 16), bg='gray', fg='brown',
                     width=15)
help_button.bind('<Button-1>', write_instructions)
help_button.pack(anchor=N)


def quit_function(event):
    global x

    window.destroy()
    x += 1


quit_button=Button(frame_home, text="Quit", relief='raised', font=('Gang of Three', 16), bg='gray', fg='brown'
                   , width=15)
quit_button.bind('<Button-1>', quit_function)
quit_button.pack(anchor=N)

frame_home.pack()

window.mainloop()