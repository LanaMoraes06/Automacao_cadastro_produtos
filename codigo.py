#Passo 1: entrar no sistema da empresa
#Passo 2: Fazer login
#Passo 3: importar a base de dados
#Passo 4: Cadastrar 1 produto
#Passo 5: Repetir o passo 4 até acabar a lista

import pyautogui
import time 
pyautogui.PAUSE = 1
#pyautogui.click -> clicar com o mouse
#pyautogui.write -> escrever um texto
#pyautogui.press -> apertar uma tecla
#pyautogui.hotkey -> apertar uma combinação de teclas (ex: Ctrl + D)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3) #tempo de espera


pyautogui.click(898, 466)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

import pandas

table = pandas.read_csv("produtos.csv")
print(table)



for linha in table.index:
    pyautogui.click(859, 321)   
    
    pyautogui.write(str(table.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "categoria"]))   
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "custo"]))
    pyautogui.press("tab") 
    obs = table.loc[linha, "obs"]
    if obs != "nan":
        pyautogui.write(str(obs))
    pyautogui.press("tab")  
    pyautogui.press("enter")
    pyautogui.scroll(8000)

