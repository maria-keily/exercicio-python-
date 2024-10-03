import tkinter as tk #biblioteca de interfa de python
from tkinter import ttk

#função para converter Celsius em Fahrenhenit
def converter ():
    try:
        celsius = float(entry_celsius.get()) #pega o valor inserido no campo de entrada
        fahrenheit = (celsius * 9/5) + 32 #conversor para fahrenheit
        label_resultado.config(text=f"{fahrenheit: .2f} °F") 
    except ValueError:
        label_resultado.config(text="Entrada inválida")
        
 #configuração da janela principal
 
janela= tk.Tk()
janela.title("conversor de Temperatura")
 
 #estilo e tamanho da janela 
 
janela.geometry("400x200") #tamanho  
janela.config(bg="#e6f2ff")  #cor de fundo  
 
 #rótulo de título
label_titulo = tk.Label(janela, text="Conversor de Celsius para Fahrenehit", font=('Helvetica',16, 'bold'), bg="#e6f2ff")
label_titulo.pack(pady=10)
 
 #frame para organizar os widgets
frame = tk.Frame(janela, bg="#e6f2ff")
frame.pack(pady=20)
 
 #campo de entrada para o valor em Celsius 
entry_celsius = ttk.Entry(frame, text="°C", font=('Helvetica', 14), width=10)
entry_celsius.grid(row=0, column=1, padx=10)
 
 #róturo para indicar o campo de entrada
label_celsius = tk.Label(frame, text="°C", font=('Helvetica', 14), bg="#e6f2ff")
label_celsius.grid(row=0, column=3, padx=10)
 
 #botão de conversão
botao_converter = ttk.Button(frame, text="Converter",command=converter)
botao_converter.grid(row=0, column=3, padx=10) #rox = linha, coluna, padx = margem
 
 #rótulo para mostrar o resultado
label_resultado = tk.Label(janela, text="", font=('Helvetica', 16), bg="#e6f2ff")
label_resultado.pack(pady=20)

janela.mainloop()
 
 