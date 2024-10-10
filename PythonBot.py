import pandas as pd
import pyautogui
import pandas
import time

# Passo 1: Entrar no sistema da empresa

#Função para abrir o navegador
def abrir_navegador():
    pyautogui.PAUSE = 1.5
    #abrir sistema
    pyautogui.press("win")
    pyautogui.write("opera")
    pyautogui.press("enter")
   # pyautogui.click(x=199, y=46)
    pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
    pyautogui.press("enter")

#Função para fazer login
def fazer_login():
    pyautogui.PAUSE = 2
    pyautogui.click(x=525, y=322)
    pyautogui.write("augustocoimbra26@hotmail.com")
    pyautogui.press("tab")
    pyautogui.write("hdwuqajsdhqwou")
    pyautogui.PAUSE = 2
    pyautogui.press("tab")
    pyautogui.press("enter")

# Função para iaugustocoimbra26@hotmail.commportar a base de produtos pra cadastrar
def exportando_tabela():
    tabela = pandas.read_csv("produtos.csv")
    print(tabela)


def exportando_dados_da_tabela():
   # pyautogui.click(x=513, y=240)
    tabela = pandas.read_csv("produtos.csv")

    linha = 0
    for linha in tabela.index:
        pyautogui.click(x=513, y=240)
        codigo = tabela.loc[linha, "codigo"]
        pyautogui.write(str(codigo))
        pyautogui.press("tab")

        marca = tabela.loc[linha, "marca"]
        pyautogui.write(str(marca))
        pyautogui.press("tab")

        tipo = tabela.loc[linha, "tipo"]
        pyautogui.write(str(tipo))
        pyautogui.press("tab")

        categoria = tabela.loc[linha, "categoria"]
        pyautogui.write(str(categoria))
        pyautogui.press("tab")

        preco_unitario = tabela.loc[linha, "preco_unitario"]
        pyautogui.write(str(preco_unitario))
        pyautogui.press("tab")

        custo = tabela.loc[linha, "custo"]
        pyautogui.write(str(custo))
        pyautogui.press("tab")

        if not pd.isna(tabela.loc[linha, "obs"]):
            pyautogui.write(str(tabela.loc[linha,"obs"]))

        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.scroll(1000000)

abrir_navegador()
time.sleep(3)
fazer_login()
time.sleep(2)
exportando_tabela()
time.sleep(2)
exportando_dados_da_tabela()

