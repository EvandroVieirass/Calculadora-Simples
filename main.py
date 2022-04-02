#importando tkinter
from tkinter import *
from tkinter import ttk


#cores 
cor1 = '#a7c9c3'#tela
cor2 = '#606b68'#fundo frame botoes
cor3 = '#9ea8a6'#botao limpar
cor4 = '#f58505'#botoes de calculo
janela = Tk()
janela.title('Calculadora')
janela.geometry('310x370')
janela.config(background='white')
janela.resizable(width=False,height=False)
frame_tela = Frame(janela,width=310,height=70,background=cor2)
frame_tela.grid(row=0,column=0)
valor_texto = StringVar()
l_tela = Label(frame_tela, textvariable=valor_texto,width=14,height=2,padx=7,relief='flat',anchor="e",justify=RIGHT,font='Helvetica 25 bold')
l_tela.place(x=7,y=7)
frame_botoes = Frame(janela,width=310,height=370,background=cor2)
frame_botoes.grid(row=1,column=0)
todos_valores = ''
def Entrar_Valores(args):
    global todos_valores
    todos_valores =todos_valores +  str(args)
    valor_texto.set(todos_valores)

def Calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    #todos_valores = str(resultado)
    todos_valores = "" 

def Limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


#criando os botoes
b_c = Button(frame_botoes,width=10,height=2,background='#9ea8a6',command=Limpar_tela,text='C',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='raise')
b_c.place(x=6,y=2)
b_porcentagem = Button(frame_botoes,width=10,height=2,background='#9ea8a6',command=lambda : Entrar_Valores('%'),text='%',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='raise')
b_porcentagem.place(x=120,y=2)
b_divisao = Button(frame_botoes,width=6,height=2,background='#9ea8a6',command=lambda : Entrar_Valores('/'),text='/',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='raise')
b_divisao.place(x=234,y=2)
b_7 = Button(frame_botoes,width=6,height=2,background='#9ea8a6',command=lambda : Entrar_Valores('7'),text='7',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='raise')
b_7.place(x=6,y=60)
b_8 = Button(frame_botoes,width=6,height=2,background='#9ea8a6',command=lambda : Entrar_Valores('8'),text='8',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='raise')
b_8.place(x=82,y=60)
b_9= Button(frame_botoes,width=6,height=2,background='#9ea8a6',command=lambda : Entrar_Valores('9'),text='9',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='raise')
b_9.place(x=158,y=60)
b_multiplicacao = Button(frame_botoes,width=6,height=2,background='#9ea8a6',command=lambda : Entrar_Valores('*'),text='*',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='raise')
b_multiplicacao.place(x=234,y=60)
b_4= Button(frame_botoes,width=6,height=2,background='#9ea8a6',command=lambda : Entrar_Valores('4'),text='4',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='raise')
b_4.place(x=6,y=118)
b_5 = Button(frame_botoes,width=6,height=2,background='#9ea8a6',command=lambda : Entrar_Valores('5'),text='5',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='raise')
b_5.place(x=82,y=118)
b_6 = Button(frame_botoes,width=6,height=2,background='#9ea8a6',command=lambda : Entrar_Valores('6'),text='6',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='raise')
b_6.place(x=158,y=118)
b_subtracao = Button(frame_botoes,width=6,height=2,background='#9ea8a6',command=lambda : Entrar_Valores('-'),text='-',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='raise')
b_subtracao.place(x=234,y=118)
b_1 = Button(frame_botoes,width=6,height=2,background='#9ea8a6',command=lambda : Entrar_Valores('1'),text='1',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='groove')
b_1.place(x=6,y=176)
b_2= Button(frame_botoes,width=6,height=2,background='#9ea8a6',command=lambda : Entrar_Valores('2'),text='2',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='raise')
b_2.place(x=82,y=176)
b_3= Button(frame_botoes,width=6,height=2,background='#9ea8a6',command=lambda : Entrar_Valores('3'),text='3',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='raise')
b_3.place(x=158,y=176)
b_somar = Button(frame_botoes,width=6,height=5,background='#9ea8a6',command=lambda : Entrar_Valores('+'),text='+',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='raise')
b_somar.place(x=234,y=176)
b_0= Button(frame_botoes,width=6,height=2,background='#9ea8a6',command=lambda : Entrar_Valores('0'),text='0',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='raise')
b_0.place(x=6,y=234)
b_ponto= Button(frame_botoes,width=6,height=2,background='#9ea8a6',command=lambda : Entrar_Valores('.'),text='.',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='raise')
b_ponto.place(x=82,y=234)
b_igual= Button(frame_botoes,command=Calcular,width=6,height=2,background='#9ea8a6',text='=',fg='white',font='Helvetica 12 bold',overrelief='flat',relief='raise')
b_igual.place(x=158,y=234)

def calcular():
    x = eval('9*3')


janela.mainloop()
