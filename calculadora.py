from tkinter import Tk, Label, Button, Entry,END,TOP


def limpa_AC():
    entrada.delete(0, END)


def igual():
    digitado = entrada.get()
    aparece = []

    if '^' in  digitado:
        num, exponente = digitado.split('^')
        aparece.append(float(num))
        aparece.append(float(exponente))
        simbolo = '^'

    elif 'x' in digitado:
        aparece = digitado.split('x')
        aparece[0] = float(aparece[0])
        aparece[1] = float(aparece[1])
        simbolo = 'x'

    elif '+' in digitado:
        aparece = digitado.split('+')
        aparece[0] = float(aparece[0])
        aparece[1] = float(aparece[1])
        simbolo = '+'
    elif '-' in digitado:
        aparece = digitado.split('-')
        aparece[0] = float(aparece[0])
        aparece[1] = float(aparece[1])
        simbolo = '-'
    elif '/' in digitado:
        aparece = digitado.split('/')
        aparece[0] = float(aparece[0])
        aparece[1] = float(aparece[1])
        simbolo = '/'
    else:
        entrada.delete(0, END)
        entrada.insert(END, "Erro")
        return

    if simbolo == '^':
        resultado = aparece[0] ** aparece[1]
    elif simbolo == 'x':
        resultado = aparece[0] * aparece[1]
    elif simbolo == '+':
        resultado = aparece[0] + aparece[1]
    elif simbolo == '-':
        resultado = aparece[0] - aparece[1]
    elif simbolo == '/':
        if aparece[1] != 0:
            resultado = aparece[0] / aparece[1]
        else:
            entrada.delete(0, END)
            entrada.insert(END, "Impossível dividir por zero")
            return

    entrada.delete(0, END)
    entrada.insert(END, str(resultado))


def clicado(op):
    digitado = entrada.get()
    entrada.delete(0, END)
    entrada.insert(END, digitado + op)


janela = Tk()
entrada = Entry(janela)
janela.geometry('330x420')

# AC BOTÃO
btn_AC = Button(janela, text="AC", command=limpa_AC)
btn_AC['background'] = '#d3d3d3'
btn_AC.place(x=13, y=90, width=130, height=50)
# NÚMERO 7 BOTÃO
btn_7 = Button(janela, text="7", command=lambda: clicado('7'))
btn_7['background'] = "#a9a9a9"
btn_7.place(x=13, y=150, width=60, height=60)
# NÚMERO 8 BOTÃO
btn_8 = Button(janela, text="8", command=lambda: clicado('8'))
btn_8['background'] = "#a9a9a9"
btn_8.place(x=85, y=150, width=60, height=60)
# NÚMERO 9 BOTÃO
btn_9 = Button(janela, text="9", command=lambda: clicado('9'))
btn_9['background'] = "#a9a9a9"
btn_9.place(x=157, y=150, width=60, height=60)
# ......................
# NÚMERO 4 BOTÃO
btn_4 = Button(janela, text="4", command=lambda: clicado('4'))
btn_4['background'] = "#a9a9a9"
btn_4.place(x=13, y=220, width=60, height=60)
# NÚMERO 5 BOTÃO
btn_5 = Button(janela, text="5", command=lambda: clicado('5'))
btn_5['background'] = "#a9a9a9"
btn_5.place(x=85, y=220, width=60, height=60)
# NÚMERO 6 BOTÃO
btn_6 = Button(janela, text="6", command=lambda: clicado('6'))
btn_6['background'] = "#a9a9a9"
btn_6.place(x=157, y=220, width=60, height=60)
# ....................................
# NÚMERO 1 BOTÃO
btn_1 = Button(janela, text="1", command=lambda: clicado('1'))
btn_1['background'] = "#a9a9a9"
btn_1.place(x=13, y=290, width=60, height=60)
# NÚMERO 2 BOTÃO
btn_2 = Button(janela, text="2", command=lambda: clicado('2'))
btn_2['background'] = "#a9a9a9"
btn_2.place(x=85, y=290, width=60, height=60)
# NÚMERO 3 BOTÃO
btn_3 = Button(janela, text="3", command=lambda: clicado('3'))
btn_3['background'] = "#a9a9a9"
btn_3.place(x=157, y=290, width=60, height=60)
# NÚMERO 0 BOTÃO
btn_0 = Button(janela, text="0", command=lambda: clicado('0'))
btn_0['background'] = "#a9a9a9"
btn_0.place(x=13, y=360, width=130, height=50)
# PONTO BOTÃO
btn_ponto = Button(janela, text=".", command=lambda: clicado('.'))
btn_ponto['background'] = "#a9a9a9"
btn_ponto.place(x=157, y=360, width=60, height=50)
# POTÊNCIA BOTÃO
btn_potencia = Button(janela, text="^", command=lambda: clicado('^'))
btn_potencia['background'] = "#ffa500"
btn_potencia.place(x=157, y=90, width=60, height=50)
# IGUAL BOTÃO
btn_igual = Button(janela, text="=", command= igual)
btn_igual['background'] = '#ffa500'
btn_igual.place(x=229, y=360, width=90, height=50)
#  MAIS BOTÃO
btn_mais = Button(janela, text="+", command=lambda: clicado('+'))
btn_mais['background'] = "#ffa500"
btn_mais.place(x=229, y=290, width=90, height=60)
#  MENOS BOTÃO
btn_menos = Button(janela, text="-", command=lambda: clicado('-'))
btn_menos['background'] = "#ffa500"
btn_menos.place(x=229, y=220, width=90, height=60)
#  MULTIPLICAÇÃO BOTÃO
btn_mult = Button(janela, text="x", command=lambda: clicado('x'))
btn_mult['background'] = "#ffa500"
btn_mult.place(x=229, y=150, width=90, height=60)
#  DIVISÃO BOTÃO
btn_div = Button(janela, text="/", command=lambda: clicado('/'))
btn_div['background'] = "#ffa500"
btn_div.place(x=229, y=90, width=90, height=50)

entrada.config(font=('Times', 30, 'bold'))
entrada['background'] = "#d3d3d3"
entrada.place(width=320, height=80)

entrada['justify'] = 'right'

janela.mainloop()
