import tkinter as TK
import tkinter.ttk as ttk
import converter
import BoxesDialogs
import random as rnd

global sizewind
sizewind = "450x650"
def nullcommand():pass


def dialogMer(mer="Время"):
    mers = {"Время":[('year', 'Г', 'год'), ('mont', 'М', 'месяц'), ('day', 'Д', 'день'), ('ned', 'Нед', 'неделя'), ('h','Ч' , 'час'), ('min', 'Мин', 'минута'), ('sec', 'Сек', 'секунда')],
            "Температура":[('C', 'Цельсия'), ('K', 'Кельвина')],
            "Длина":[('km', 'км', 'километр'), ('m', 'м', 'метр'), ('cm', 'см', 'сантиметр'), ('mm', 'мм', 'милиметр')],
            "Весы":[('t', 'т', 'тонна'), ('c', 'ц', 'центнер'), ('kg', 'кг', 'килограмм'), ('g', 'г', 'грамм'), ('mg', 'мг', 'милиграмм')],
            "Площадь":[('km', 'кв.км', 'кв.километр'), ('m', 'кв.м', 'кв.метр'), ('cm', 'Кв.см', 'кв.сантиметр')],
            "Объём":[('m', 'Куб.м', 'куб.метр'), ('dm', 'Л', 'литр'), ('cm', 'Куб.См', 'куб.сантиметр')],
            "Скорость":[],
            "Системы счислений":[('10', '10-ич'), ('3', '3-ич'), ('2', '2-ич'), ('12', '12-ич'), ('6', '6-ич'), ('15', '15-ич'), ('18', '18-ич')],
            "Углы":[('g', 'Градусы'), ('r', 'Радианы')],
            "Анаграммы":'Combinatorics',
            "Сочетания C":'Combinatorics',
            "Сочетания A":'Combinatorics',
            "Сочетания с \nповторениями":'Combinatorics',
            'P(elems)':'Combinatorics',
            'Каталан':'Combinatorics'}
    if len(mers[mer]) == 0:
        BoxesDialogs.MessageDialog(title="Ошибка", textmessage="Измерения не найдены", buttons=['OK'], commands=[nullcommand])
        return
    funs = {'Время':converter.timer, 'Длина':converter.lener,
            'Температура':converter.temperature, 'Весы':converter.massa,
            'Объём':converter.objom, 'Площадь':converter.squares,
            "Системы счислений":converter.systemischisl,
            "Углы":converter.anglesser,
            # "Анаграммы": 'Combinatorics',
            # "Сочетания C": 'Combinatorics',
            # "Сочетания A": 'Combinatorics',
            # "Сочетания с \nповторениями": 'Combinatorics',
            # 'P(elems)': 'Combinatorics',
            # 'Каталан': 'Combinatorics'
            }
    if mer not in funs and mers[mer] == 'Combinatorics':
        w = TK.Tk(className="Меры")
        w.configure(bg='black')
        # w.geometry("520x570")
        spfr = TK.Frame(w, bg='black')
        def back():
            w.destroy()
            opcions()

        TK.Button(spfr, text="<", bg='black', fg='white', font='Arial 16', command=back).pack(side="left")
        TK.Label(spfr, text=mer, bg='black', fg='white', font='Arial 18').pack(side="right")
        spfr.pack(fill=TK.X)
        bt = TK.Frame(w, bg='black')
        activy = ''
        if 'Сочетан' in mer:
            m1 = TK.Menubutton(bt, text='k=', bg='black',
                               fg='orange', font="Arial 20")

            m1.grid(row=1, column=0)
            k_sel = TK.Entry(bt, bg='black', fg='white', font="Arial 22",
                             width=5)
            k_sel.grid(row=1, column=1)
            n_sel = TK.Entry(bt, bg='black', fg='orange', font="Arial 20",
                             width=6)
            n_sel.grid(row=2, column=1)
            m2 = TK.Menubutton(bt, text='n=', bg='black',
                               fg='orange', font="Arial 20")
            m2.grid(row=2, column=0)
            TK.Label(bt, text=(mer[-1] if mer[-1] != 'и' else f'_\nC'), bg='black', fg='white',
                            font='Arial 19').grid(row=4, column=0)
            itog2 = TK.Label(bt, text='', bg='black', fg='white',
                            font='Arial 19')
            itog = TK.Label(bt, text='', bg='black', fg='white',
                            font='Arial 19')
            itog.grid(row=4, column=2)
            itog2.grid(row=4, column=1)

            def evaluter():
                itog2['text'] = f'{k_sel.get()}\n{n_sel.get()}'
                itog['text'] = '= '
                if mer.endswith('C'):
                    itog['text'] += str(converter.comb(int(n_sel.get()
                                                          ), int(k_sel.get())))
                elif mer.endswith('A'):
                    itog['text'] += str(converter.comb3(int(n_sel.get()
                                                          ), int(k_sel.get())))
                elif mer.endswith('повторениями'):
                    itog['text'] += str(converter.comb2(int(n_sel.get()
                                                           ), int(k_sel.get())))

            TK.Button(bt, text='=', bg='black', fg='red',
                      font='Arial 20', command=evaluter).grid(row=3, column=0)
            bt.pack(fill=TK.X)
        else:
            m1 = TK.Menubutton(bt, text='C', bg='black',
                               fg='orange', font="Arial 20")
            m1.grid(row=1, column=0)
            activy = TK.Label(bt, text='\n', bg='black', fg='white', font='Arial 21')
            activy.grid(row=1, column=1)
            res = TK.Label(bt, text='', bg='black', fg='orange', font='Arial 20')
            def evalute():
                res['text'] = '= '
                res['text'] += str(converter.catalan(int(activy['text'])))
            res.grid(row=1, column=2)
            bt.pack(fill=TK.X)
            claviature = TK.Frame(w, bg="black")
            TK.Button(claviature, text='CLR', bg='black',
                      fg='orange', width=2, height=2, font="Arial 15", command=lambda x=0: activy.config(text="\n")).grid(
                row=0, column=0)
            TK.Button(claviature, text="1", bg="black", fg="orange",
                      width=2, height=2, command=lambda x=1: activy.config(text=activy["text"] + '1'),
                      font="Arial 17").grid(row=1, column=0)
            TK.Button(claviature, text="2", bg="black", fg="orange",
                      width=2, height=2, font="Arial 17",
                      command=lambda x=1: activy.config(text=activy["text"] + '2')).grid(row=1, column=1)
            TK.Button(claviature, text="3", bg="black", fg="orange",
                      width=2, height=2, font="Arial 17",
                      command=lambda x=1: activy.config(text=activy["text"] + '3')).grid(row=1, column=2)
            TK.Button(claviature, text="4", bg="black", fg="orange",
                      width=2, height=2, font="Arial 17",
                      command=lambda x=1: activy.config(text=activy["text"] + '4')).grid(row=2, column=0)
            TK.Button(claviature, text="5", bg="black", fg="orange",
                      width=2, height=2, font="Arial 17",
                      command=lambda x=1: activy.config(text=activy["text"] + '5')).grid(row=2, column=1)
            TK.Button(claviature, text="6", bg="black", fg="orange",
                      width=2, height=2, font="Arial 17",
                      command=lambda x=1: activy.config(text=activy["text"] + '6')).grid(row=2, column=2)
            TK.Button(claviature, text="7", bg="black", fg="orange",
                      width=2, height=2, font="Arial 17",
                      command=lambda x=1: activy.config(text=activy["text"] + '7')).grid(row=3, column=0)
            TK.Button(claviature, text="8", bg="black", fg="orange",
                      width=2, height=2, font="Arial 17",
                      command=lambda x=1: activy.config(text=activy["text"] + '8')).grid(row=3, column=1)
            TK.Button(claviature, text="9", bg="black", fg="orange",
                      width=2, height=2, font="Arial 17",
                      command=lambda x=1: activy.config(text=activy["text"] + '9')).grid(row=3, column=2)
            TK.Button(claviature, text="0", bg="black", fg="orange",
                      width=2, height=2, font="Arial 17",
                      command=lambda x=1: activy.config(text=activy["text"] + '0')).grid(row=4, column=1)
            TK.Button(claviature, text="=", bg="black", fg="orange",
                      width=2, height=2, font="Arial 17", command=evalute).grid(row=4, column=2)
            claviature.pack(fill=TK.X)
    else:

        valuesconv = mers[mer]
        functionmer = funs[mer]

        w = TK.Tk(className="Меры")
        w.configure(bg='black')
        #w.geometry("520x570")
        spfr = TK.Frame(w, bg='black')
        def back():
            w.destroy()
            opcions()
        TK.Button(spfr, text="<", bg='black', fg='white', font='Arial 16', command=back).pack(side="left")
        TK.Label(spfr, text=mer, bg='black', fg='white', font='Arial 18').pack(side="right")
        bt = TK.Frame(w, bg='black')
        spfr.pack(fill=TK.X)
        # TK.Label(w,
        #          text="Если возвращена константа inf, \nто это значит что результат\nлибо не найден, либо превышает 10**10",
        #          bg='yellow', fg='black', font='Arial 14').pack(fill=TK.X)
        m1 = TK.Menubutton(bt, text=valuesconv[0][1], bg='black',
                           fg='orange', font="Arial 20")
        menu1 = TK.Menu(m1, tearoff=0, bg='black', fg='orange', font='Arial 14')
        for i in valuesconv:
            if len(i) > 2:
                menu1.add_command(label=(i[2] if len(i)>1 else ''), command=lambda x=i[1]:m1.config(text=x))
            else:
                menu1.add_command(label=i[1],
                                  command=lambda x=i[1]: m1.config(text=x))
        m1.config(menu=menu1)
        m1.grid(row=1, column=0)
        n_sel = TK.Label(bt, bg='black', fg='white', font="Arial 22")
        n_sel.grid(row=1, column=1)
        k_sel = TK.Label(bt, bg='black', fg='orange', font="Arial 24")
        k_sel.grid(row=2, column=1)
        m2 = TK.Menubutton(bt, text=valuesconv[1][1], bg='black',
                           fg='orange', font="Arial 20")
        menu2 = TK.Menu(m2, tearoff=0, bg='black', fg='orange', font='Arial 14')
        for i in valuesconv:
            if len(i) > 2:
                menu2.add_command(label=(i[2] if len(i)>1 else ''), command=lambda x=i[1]:m2.config(text=x))
            else:
                menu2.add_command(label=i[1],
                                  command=lambda x=i[1]: m2.config(text=x))
        m2.configure(menu=menu2)
        m2.grid(row=2, column=0)
        bt.pack(fill=TK.X)
        dopmenu = TK.Frame(w, bg='black')
        # TK.Button(dopmenu, text='←', bg='black',
        #           fg='orange', width=2, height=2,font="Arial 17", command=lambda x=0:n_sel.config(text=n_sel["text"][:-1])).grid(row=0, column=0)
        # TK.Button(dopmenu, text='(', bg='black',
        #           fg='orange', width=2, height=2,font="Arial 17", command=lambda x=0: resulter.config(text=resulter["text"]+'(')).grid(row=0, column=1)
        # TK.Button(dopmenu, text=')', bg='black',
        #           fg='orange', width=2, height=2,font="Arial 17", command=lambda x=0: resulter.config(text=resulter["text"]+')')).grid(row=0, column=2)
        def convertMer():
            pos1 = 0
            pos2 = 0
            j=0
            for i in valuesconv:
                if i[1] == m1["text"]:
                    pos1 = j
                elif i[1] == m2["text"]:
                    pos2 = j
                j+=1


            x = functionmer(int(n_sel["text"]), valuesconv[pos1][0], valuesconv[pos2][0])
            k_sel.config(text=x)
        TK.Button(dopmenu, text='CLR', bg='black',
                  fg='orange', width=2, height=2,font="Arial 15", command=lambda x=0: n_sel.config(text="")).grid(row=0, column=3)
        TK.Button(dopmenu, text='', bg='black',
                  fg='orange', width=2, height=2, font="Arial 15").grid(row=0,                                                                                                     column=4)
        dopmenu.pack(fill=TK.X)
        claviature = TK.Frame(w, bg="black")
        TK.Button(claviature, text="1", bg="black", fg="orange",
                  width=2, height=2, command=lambda x=1: n_sel.config(text=n_sel["text"] + '1'),
                  font="Arial 17").grid(row=0, column=0)
        TK.Button(claviature, text="2", bg="black", fg="orange",
                  width=2, height=2, font="Arial 17",
                  command=lambda x=1: n_sel.config(text=n_sel["text"] + '2')).grid(row=0, column=1)
        TK.Button(claviature, text="3", bg="black", fg="orange",
                  width=2, height=2, font="Arial 17",
                  command=lambda x=1: n_sel.config(text=n_sel["text"] + '3')).grid(row=0, column=2)
        TK.Button(claviature, text="4", bg="black", fg="orange",
                  width=2, height=2, font="Arial 17",
                  command=lambda x=1: n_sel.config(text=n_sel["text"] + '4')).grid(row=1, column=0)
        TK.Button(claviature, text="5", bg="black", fg="orange",
                  width=2, height=2, font="Arial 17",
                  command=lambda x=1: n_sel.config(text=n_sel["text"] + '5')).grid(row=1, column=1)
        TK.Button(claviature, text="6", bg="black", fg="orange",
                  width=2, height=2, font="Arial 17",
                  command=lambda x=1: n_sel.config(text=n_sel["text"] + '6')).grid(row=1, column=2)
        TK.Button(claviature, text="7", bg="black", fg="orange",
                  width=2, height=2, font="Arial 17",
                  command=lambda x=1: n_sel.config(text=n_sel["text"] + '7')).grid(row=2, column=0)
        TK.Button(claviature, text="8", bg="black", fg="orange",
                  width=2, height=2, font="Arial 17",
                  command=lambda x=1: n_sel.config(text=n_sel["text"] + '8')).grid(row=2, column=1)
        TK.Button(claviature, text="9", bg="black", fg="orange",
                  width=2, height=2, font="Arial 17",
                  command=lambda x=1: n_sel.config(text=n_sel["text"] + '9')).grid(row=2, column=2)
        TK.Button(claviature, text="0", bg="black", fg="orange",
                  width=2, height=2, font="Arial 17",
                  command=lambda x=1: n_sel.config(text=n_sel["text"] + '0')).grid(row=3, column=1)
        TK.Button(claviature, text="=", bg="black", fg="orange",
                  width=2, height=2, font="Arial 17", command=convertMer).grid(row=3, column=2)
        claviature.pack(fill=TK.X)#, side="bottom")

    w.mainloop()
def calcdates():
    dates = TK.Tk(className="Расчёт дат")
    def back():
        dates.destroy()
        opcions()
    TK.Button(dates, text="Закрыть", bg='red', fg='white', command=back).pack(fill=TK.X)
    TK.Label(dates, bg='white', text="Укажите дату в формате ДД.ММ.ГГГГ").pack(fill=TK.X)
    e1 = TK.Entry(dates, font="Arial 15")
    e1.pack(fill=TK.X)
    TK.Label(dates, bg='white', text="Укажите дату в формате ДД.ММ.ГГГГ").pack(fill=TK.X)
    e2 = TK.Entry(dates, font="Arial 15")
    e2.pack(fill=TK.X)
    def minusdates():
        pass
    TK.Button(dates, text="Расчитать", bg='blue', fg='white', command=minusdates).pack(fill=TK.X)
    dates.mainloop()
def openimageph(filer):
    imc = TK.Tk(className="Изображение")
    imc.config(bg='black')
    spfr = TK.Frame(imc, bg='black')
    def back():
        imc.destroy()
        mybirds()
    TK.Button(spfr, text="<", bg='black', fg='white', font='Arial 16', command=back).pack(side="left")
    TK.Label(spfr, text="Просмотр птицы", bg='black', fg='white', font='Arial 18').pack(side="right")
    spfr.pack(fill=TK.X)
    ph = TK.PhotoImage(file=filer+'.png', master=imc)
    TK.Label(imc, image=ph, bg='black').pack(fill=TK.X)
    imc.mainloop()
def mybirds():
    with open('birdscalc.txt', 'r') as flg:
        icons = flg.read().split(';')
    with open('historycalc.txt', 'r') as flhist:
        ln = len(flhist.read().split(';'))
    birdser = TK.Tk(className="Мои птицы")
    birdser.config(bg='black')
    global sizewind
    birdser.geometry(sizewind)

    def getbirder():
        with open('birds.txt', 'r') as flgh:
            brs = flgh.read().split(';')
        with open('problemsert.txt', 'r') as flpr:
            problm = flpr.read().split(';')
        p1 = rnd.choice(problm).split('&')
        p2 = rnd.choice(problm).split('&')
        birdser.destroy()

        birdnew = TK.Tk(className="Получение птицы")

        def checktest():
            if p1[1] == e1.get() and p2[1] == e2.get():
                # BoxesDialogs.MessageDialog(title="Готово", textmessage="Вы получили ещё 1 птицу!", buttons=['Хорошо'])
                with open('birdscalc.txt', 'a') as flh:
                    flh.write(';' + cm.get())
                BoxesDialogs.MessageDialog(title="Готово", textmessage="Вы получили ещё 1 птицу!", buttons=['Хорошо'],
                                           commands=[birdnew.destroy])
                if ln < len(icons)*2-1:
                    gp.destroy()
            else:
                birdnew.destroy()
                mybirds()

        TK.Label(birdnew, text="Выберете птицу которую Вы хотите:", bg='white', font="Arial 15").pack(fill=TK.X)
        cm = ttk.Combobox(birdnew, values=brs)
        cm.pack(fill=TK.X)
        TK.Label(birdnew, text=p1[0], bg='white', font="Arial 12").pack(fill=TK.X)
        e1 = TK.Entry(birdnew, font="Arial 12")
        e1.pack(fill=TK.X)
        TK.Label(birdnew, text=p2[0], bg='white', font="Arial 12").pack(fill=TK.X)
        e2 = TK.Entry(birdnew, font="Arial 12")
        e2.pack(fill=TK.X)
        TK.Button(birdnew, text="Проверить", bg='blue', fg='white', command=checktest).pack(fill=TK.X)
        birdnew.mainloop()
    def back():
        birdser.destroy()
        opcions()
    spfr = TK.Frame(birdser, bg='black')
    TK.Button(spfr, text="<", bg='black', fg='white', font='Arial 16', command=back).pack(side="left")
    TK.Label(spfr, text="Мои птицы", bg='black', fg='white', font='Arial 18').pack(side="right")
    spfr.pack(fill=TK.X)
    if ln >= len(icons)*2-1:
        gp = TK.Button(birdser, text="Получить птицу", bg='blue', fg='white', command=getbirder)
        gp.pack(fill=TK.X)
    else:
        TK.Label(birdser, text="Для того чтобы получить птицу\n надо сделать "+str(len(icons)*2-1)+" вычислений", bg='red', fg='white').pack(fill=TK.X)
    imageser = []
    j=0
    def openimageer(x):
        birdser.destroy()
        openimageph(x)

    for i in icons:
        imageser.append(TK.Button(birdser, text=i, bg='white', fg='black', command=lambda x=i:openimageer(x), width=30, height=2))
        imageser[j].pack(fill=TK.X)
        j += 1
    birdser.mainloop()
def history():
    with open('historycalc.txt', 'r') as flhist:
        hist = flhist.read().split(';')
    hs = TK.Tk(className="История")
    hs.config(bg='black')
    global sizewind
    hs.geometry(sizewind)
    def back():
        hs.destroy()
        opcions()
    spfr = TK.Frame(hs, bg='black')
    TK.Button(spfr, text="<", bg='black', fg='white', font='Arial 16', command=back).pack(side="left")
    TK.Label(spfr, text="История", bg='black', fg='white', font='Arial 18').pack(side="right")
    spfr.pack(fill=TK.X)
    for i in hist:
        TK.Label(hs, text=i, bg='black', font="Arial 16", fg='white').pack(fill=TK.X)
    hs.mainloop()
def opcions():
    with open('settingscalc.txt', 'r') as fld:
        ls = fld.read().split(';')[1].split('&')
    with open('settingscalc.txt', 'r') as flhist:
        ishisory = flhist.read().split(';')[0] == '1'
    opc = TK.Tk(className="Конвертер")
    opc.config(bg='black')
    global sizewind
    opc.geometry(sizewind)
    spfr = TK.Frame(opc, bg='black')
    def back():
        opc.destroy()
        start()
    TK.Button(spfr, text="<", bg='black', fg='white', font='Arial 16', command=back).pack(side="left")
    TK.Label(spfr, text="Конверты", bg='black', fg='white', font='Arial 18').pack(side="right")
    spfr.pack(fill=TK.X)
    #ls = ["Объём", 'Время', "Весы", "Температура", "Длина", "Площадь", "Скорость"]
    ls += ['Сочетания C', 'Каталан', 'Сочетания A', 'Сочетания с \nповторениями',
           'P (elems)', 'Анаграммы']

    paned = TK.Frame(opc, bg='black')
    lbc = []
    j=0
    wd = 10
    def openmera(value):
        opc.destroy()
        dialogMer(value)
    for elem in ls:
        lbc.append(TK.Button(paned, text=elem, bg='black', fg='white', command=lambda x=elem:openmera(x), height=2, width=wd))
        lbc[j].grid(row=j//3, column=j%3)
        j+=1
    # TK.Button(paned, text="Транспортир", bg='black', fg='orange', width=wd, height=2, command=lambda x=0:converter.angledraw()).grid(row=(j+0)//3, column=(j+0)%3)
    # j+=1
    def opendates():
        opc.destroy()
        calcdates()
    TK.Button(paned, text="Расчёт дат", bg='black', fg='white', width=wd, height=2,command=opendates).grid(row=(j + 0) // 3, column=(j + 0) % 3)
    j+=1
    def openbirdser():
        opc.destroy()
        mybirds()
    TK.Button(paned, text="Мои птицы", bg='black', fg='orange', width=wd, height=2,command=openbirdser).grid(row=(j + 0) // 3, column=(j + 0) % 3)
    j += 1
    def systemschil():
        opc.destroy()
        dialogMer("Системы счислений")
    TK.Button(paned, text="Системы\nсчислений", bg='black', fg='white', width=wd, height=2, command=systemschil).grid(row=(j + 0) // 3, column=(j + 0) % 3)
    def openhistory():
        opc.destroy()
        history()
    if ishisory:
        j += 1
        TK.Button(paned, text="История", bg='black', fg='orange', width=wd, height=2, command=openhistory).grid(row=(j + 0) // 3, column=(j + 0) % 3)

    paned.pack(fill=TK.X)
    opc.mainloop()

def settings():
    with open('settingscalc.txt', 'r') as flset:
        rgeneral = flset.read().split(';')
    entrs = []
    setting = TK.Tk(className="Настройки")
    setting.config(bg='black')
    global sizewind
    setting.geometry(sizewind)
    global historon
    historon = rgeneral[0]=='1'
    def savesettingsrg():
        d = []
        rg = rgeneral[1].split('&')
        num = 0
        for i in rg:
            d.append(i)
        s = ""
        if historon:s += '1'
        else:s += '0'
        s += ';'
        for it in entrs:
            s += d[int(it.get())-1] + '&'
        s = s[:-1]
        #print(s)
        with open('settingscalc.txt', 'w') as flsetgen:
            flsetgen.write(s)
        setting.destroy()
        myaccount('90')
    def historbutmen():
        global historon
        if historon:
            historon = not historon
            histor.config(text="История (выкл.)")
        else:
            historon = not historon
            histor.config(text="История (вкл.)")
    def back():
        setting.destroy()
        myaccount('0')
    TK.Label(setting, bg='blue', fg='white', text="Настройки калькулятора").pack(fill=TK.X)
    TK.Button(setting, bg='blue', text="Сохранить", fg='white', command=savesettingsrg).pack(fill=TK.X)
    TK.Button(setting, bg='red', text="Закрыть", fg='white', command=back).pack(fill=TK.X)
    TK.Label(setting, bg='white', fg='white', text="   ", height=2).pack(fill=TK.X)
    histor = TK.Button(setting, bg='white', text="История (выкл.)", relief="groove", command=historbutmen)
    if historon:
        histor.config(text="История (вкл.)")
    histor.pack(fill=TK.X)
    mapbuf= TK.Frame(setting, bg='white')
    j=0
    crpor = rgeneral[1].split('&')
    ind = 0
    for i in crpor:
        TK.Label(mapbuf, text=i, bg='white').grid(row=j//2, column=0)
        entrs.append(TK.Entry(mapbuf, bg='white'))
        entrs[ind].insert(1, str(ind+1))
        entrs[ind].grid(row=j//2, column=1)
        j+=2
        ind+=1
    mapbuf.pack(fill=TK.X)
    setting.mainloop()
def myaccount(name):
    with open('activeprofilecalc.txt', 'r') as fljk:
        name = fljk.read()
    def logout():
        with open('activeprofilecalc.txt', 'w') as fld:
            fld.write('?')
        exit()
    myd = TK.Tk(className="Аккаунт")
    global sizewind
    myd.geometry(sizewind)
    def back():
        myd.destroy()
        start()

    def about():
        def nback():
            start()
        myd.destroy()
        BoxesDialogs.MessageDialog(title="О программе", textmessage="Калькулятор\nЖуравлина книга:v.2.1\nВерсия:v.1.7",
                                   buttons=['Закрыть'], commands=[nback])
    myd.config(bg='black')
    TK.Label(myd, text="Журавлиная книга.Утилиты", bg='black', font='Arial 20', fg='white').pack(fill=TK.X)
    ic = TK.PhotoImage(file='icon.png', master=myd)
    TK.Label(myd, image=ic, bg='black').pack()
    TK.Label(myd, text="Калькулятор", bg='black', font='Arial 17', fg='white').pack(fill=TK.X)
    TK.Label(myd, text=name, bg='black', font='Arial 21', fg='white').pack(fill=TK.X)
    def opensettings():
        myd.destroy()
        settings()
    TK.Button(myd, text="Настройки", bg='black', font='Arial 15', command=opensettings, fg='white').pack(fill=TK.X)
    TK.Button(myd, text="О программе", bg='black', font='Arial 15', command=about, fg='white').pack(fill=TK.X)
    TK.Button(myd, text="Закрыть", bg='black', font='Arial 15', command=back, fg='white').pack(side='left')
    TK.Button(myd, text="Выйти", bg='black', font='Arial 15', command=logout, fg='white').pack(side='right')
    myd.mainloop()
def start(acoount="?"):
    with open('activeprofilecalc.txt', 'r') as fl2:
        r = fl2.read()
    account = r
    calc = TK.Tk(className="Калькулятор")
    calc.configure(bg="black")
    global sizewind
    calc.geometry(sizewind)
    fr = TK.Frame(calc, bg="black")
    def openopc():
        calc.destroy()
        opcions()
    def showacmenu():
        calc.destroy()
        myaccount(account)
    TK.Button(fr, text="Опции", bg="orange", command=openopc).pack(side="left")
    TK.Button(fr, text=account, bg="black",fg='white', command=showacmenu).pack(side="right")
    fr.pack(fill=TK.X, side="top")
    expressioner = TK.Frame(calc, bg='black')
    previos = TK.Label(expressioner, bg='black', fg='white', font="Arial 16")
    previos.grid(row=0, column=0)
    resulter = TK.Label(expressioner, bg="black", fg="white", font="Arial 22")
    resulter.grid(row=1, column=0)
    itog = TK.Label(expressioner, bg="black", fg="white", font="Arial 35")
    itog.grid(row=2, column=0)
    expressioner.pack(fill=TK.X)
    def calculateexpr():
        previos.config(text=resulter["text"])
        rx = resulter["text"]
        s = ""
        for i in rx:
            if i == '÷':
                s += '/'
            elif i == 'x':
                s += '*'
            elif i == ',':
                s += '.'
            else:
                s += i
        try:
            if s.isdigit():
                r2 = s
                resulter.configure(text=r2)
            else:
                r = eval(s)
                # if fl:
                #     r2 = "{:.2f}".format(int(ev))
                # else:
                #     r2 = r
                if type(r) == float:
                    r2 = "{:.2f}".format(r)
                else:
                    r2 = r
                resulter.configure(text=r2)
                with open('historycalc.txt', 'a') as flhistr:
                    flhistr.write(';')
        except (ValueError, SyntaxError, ZeroDivisionError, TypeError):
            resulter.config(text="SyntaxError")

    dopmenu = TK.Frame(calc, bg='black')
    TK.Button(dopmenu, text='←', bg='black',
              fg='orange', width=2, height=2,font="Arial 17", command=lambda x=0:resulter.config(text=resulter["text"][:-1])).grid(row=0, column=0)
    TK.Button(dopmenu, text='(', bg='black',
              fg='orange', width=2, height=2,font="Arial 17", command=lambda x=0: resulter.config(text=resulter["text"]+'(')).grid(row=0, column=1)
    TK.Button(dopmenu, text=')', bg='black',
              fg='orange', width=2, height=2,font="Arial 17", command=lambda x=0: resulter.config(text=resulter["text"]+')')).grid(row=0, column=2)
    TK.Button(dopmenu, text='CLR', bg='black',
              fg='orange', width=2, height=2,font="Arial 15", command=lambda x=0: resulter.config(text="")).grid(row=0, column=3)
    dopmenu.pack(fill=TK.X)

    claviature = TK.Frame(calc, bg="black")
    TK.Button(claviature, text="7", bg="black", fg="orange",
              width=2, height=2, command=lambda x=1:resulter.config(text=resulter["text"]+'7'),
              font="Arial 17").grid(row=0, column=0)
    TK.Button(claviature, text="8", bg="black", fg="orange",
              width=2, height=2, font="Arial 17",
              command=lambda x=1:resulter.config(text=resulter["text"]+'8')).grid(row=0, column=1)
    TK.Button(claviature, text="9", bg="black", fg="orange",
              width=2, height=2,font="Arial 17",
              command=lambda x=1:resulter.config(text=resulter["text"]+'9')).grid(row=0, column=2)
    TK.Button(claviature, text="4", bg="black", fg="orange",
              width=2, height=2,font="Arial 17", command=lambda x=1:resulter.config(text=resulter["text"]+'4')).grid(row=1, column=0)
    TK.Button(claviature, text="5", bg="black", fg="orange",
              width=2, height=2,font="Arial 17", command=lambda x=1:resulter.config(text=resulter["text"]+'5')).grid(row=1, column=1)
    TK.Button(claviature, text="6", bg="black", fg="orange",
              width=2, height=2,font="Arial 17", command=lambda x=1:resulter.config(text=resulter["text"]+'6')).grid(row=1, column=2)
    TK.Button(claviature, text="1", bg="black", fg="orange",
              width=2, height=2,font="Arial 17", command=lambda x=1:resulter.config(text=resulter["text"]+'1')).grid(row=2, column=0)
    TK.Button(claviature, text="2", bg="black", fg="orange",
              width=2, height=2,font="Arial 17", command=lambda x=1:resulter.config(text=resulter["text"]+'2')).grid(row=2, column=1)
    TK.Button(claviature, text="3", bg="black", fg="orange",
              width=2, height=2,font="Arial 17", command=lambda x=1:resulter.config(text=resulter["text"]+'3')).grid(row=2, column=2)
    TK.Button(claviature, text="0", bg="black", fg="orange",
              width=2, height=2,font="Arial 17", command=lambda x=1: resulter.config(text=resulter["text"] + '0')).grid(row=3, column=1)

    TK.Button(claviature, text=u"\u00F7", command=lambda x=1:resulter.config(text=resulter["text"]+u'\u00F7'),
              height=2, width=2,font="Arial 17", bg='black', fg='orange').grid(row=0, column=3)
    TK.Button(claviature, text="x", command=lambda x=1: resulter.config(text=resulter["text"] + 'x'),
              height=2, width=2,font="Arial 17", bg='black', fg='orange').grid(row=1, column=3)
    TK.Button(claviature, text="+", command=lambda x=1: resulter.config(text=resulter["text"] + '+'),
              height=2, width=2,font="Arial 17", bg='black', fg='orange').grid(row=2, column=3)
    TK.Button(claviature, text="-", command=lambda x=1: resulter.config(text=resulter["text"] + '-'),
              height=2, width=2,font="Arial 17", bg="black", fg='orange').grid(row=3, column=3)
    TK.Button(claviature, text=",", command=lambda x=1: resulter.config(text=resulter["text"] + ','),
              height=2, width=2,font="Arial 17", bg="black", fg='orange').grid(row=3, column=0)
    TK.Button(claviature, text="=", bg="black", fg="orange",
              width=2, height=2,font="Arial 17", command=calculateexpr).grid(row=3, column=2)
    claviature.pack(fill=TK.X)
    calc.mainloop()
def authpagelog():
    with open('activeprofilecalc.txt', 'r') as flprofact:
        r=flprofact.read()
    if r != '?' and r != '':
        start(r)
    else:
        with open('profilecalc.txt', 'r') as flaccounts:
            rdpr = flaccounts.read().split(';')
        auw= TK.Tk(className="Калькулятор")
        auw.configure(bg='#e3e3e3')
        d = {}
        for i in rdpr:
            rt = i.split('&')
            d[rt[0]] = (rt[1], rt[2])
        def strtauth():
            if acount.get() in d:
                if e1.get() == d[acount.get()][0]:
                    with open('activeprofilecalc.txt', 'w') as flacact:
                        flacact.write(d[acount.get()][1])

                    start(d[acount.get()][1])
        TK.Label(auw, text='Калькулятор\nДобро пожаловать!', bg='white').pack(fill=TK.X)
        acount = ttk.Combobox(auw, values=list(d.keys()), state="readonly", background='white',
                              )
        acount.pack(fill=TK.X)
        e1 = TK.Entry(auw, font="Arial 16", fg='white', selectbackground='white', selectforeground='white')
        e1.pack(fill=TK.X)
        TK.Button(auw, text="Войти", bg='white', command=strtauth).pack(fill=TK.X)
        auw.mainloop()
if __name__ == "__main__":
    authpagelog()
