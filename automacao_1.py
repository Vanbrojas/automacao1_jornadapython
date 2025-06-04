import pyautogui
import time
import pyperclip


url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyperclip.copy(url)

#pyautogui.hotkey('cmd', 'space') 
pyautogui.keyDown('command')  # segura a tecla command
pyautogui.press('space')      # pressiona a tecla space enquanto o command está segurado
pyautogui.keyUp('command')    # solta a tecla command

 # Abre o Spotlight no macOS
pyautogui.PAUSE = 0.5
pyautogui.write("chrome") 
pyautogui.press('return')  # Aguarda um segundo para o Spotlight abrir  chrome

pyautogui.keyDown('command')
pyautogui.press('v')
pyautogui.keyUp('command')
pyautogui.press('return')  # Pressiona Enter para abrir o link copiado
time.sleep(3)  # Aguarda a página carregar

#fazer o login detalhe, meu macbook tem o teclado em japones entao tem que copiar e colar o login e senha
pyautogui.click(616,406)  # Clica na página para garantir que o foco está nela
login = "van.brojas@gmail.com"
pyperclip.copy(login)
pyautogui.keyDown('command')
pyautogui.press('v')  # Cola o login
pyautogui.keyUp('command')
pyautogui.press('tab')  # Move para o próximo campo
pyautogui.write("123456")  # Digita a senha
pyautogui.press('return')  # Pressiona Enter para fazer login
time.sleep(3)  # Aguarda a página carregar após o login

#Importar base de dados
import pandas as pd

tabela = pd.read_csv('produtos.csv') # Carrega a tabela de produtos
 # Exibe a tabela no console para verificação
 
# adicionar o produto vai ter que repetir muitas vezes, para cada linha


#pyautogui.write(tabela.loc[0, 'codigo'])  # Digita o nome do primeiro produto
#pyautogui.press('tab')  # Move para o próximo campo
#pyautogui.write(tabela.loc[0, 'marca'])  # Digita a descrição do primeiro produto
#pyautogui.press('tab')  # Move para o próximo campo
#pyautogui.write(tabela.loc[0, 'tipo'])  # Digita o preço do primeiro produto - ler como numero (srt)
#pyautogui.press('tab')  # Move para o próximo campo
#pyautogui.write(str(tabela.loc[0, 'categoria']))  # Digita a quantidade do primeiro produto
#pyautogui.press('tab')  # Move para o próximo campo
#pyautogui.write(str(tabela.loc[0, 'preco_unitario']))  # Digita a unidade do primeiro produto
#pyautogui.press('tab')  # Move para o próximo campo
#pyautogui.write(str(tabela.loc[0, 'custo'])) # Digita o fornecedor do primeiro produto
#pyautogui.press('tab')  # Move para o próximo campo
#pyautogui.write(str(tabela.loc[0, 'obs']))
#pyautogui.press('tab') # Digita as observações do primeiro produto # Move para o próximo campo
#pyautogui.click(809, 537)
#pyautogui.click(809, 537)
#time.sleep(5)
#pyautogui.scroll(10000) #sobe até o inicio da pagina de novo, se fosse - descia  # Aguarda a página carregar após salvar o produto  


#reperir para todos as linhas, mais inteligente:
for linha in tabela.index: #index significa linha
    pyautogui.click(568, 282) 
    coluna = 'codigo'
    pyautogui.write(tabela.loc[linha, coluna])  # Digita o código do produto
    pyautogui.press('tab')  
    # Move para o próximo campo
    coluna = 'marca'
    pyautogui.write(tabela.loc[linha, coluna])  # Digita a marca do produto
    pyautogui.press('tab') # Move para o próximo campo
    coluna = 'tipo'
    pyautogui.write(str(tabela.loc[linha, coluna]))  # Digita o tipo do produto
    pyautogui.press('tab')  # Move para o próximo campo
    coluna = 'categoria'
    pyautogui.write(str(tabela.loc[linha, coluna]))  # Digita a categoria do produto
    pyautogui.press('tab')  # Move para o próximo campo
    coluna = 'preco_unitario'
    pyautogui.write(str(tabela.loc[linha, coluna]))  # Digita o preço unitário do produto
    pyautogui.press('tab')  # Move para o próximo campo
    coluna = 'custo'
    pyautogui.write(str(tabela.loc[linha, coluna]))  # Digita o custo do produto
    pyautogui.press('tab')  # Move para o próximo campo
    coluna = 'obs'
    if pd.notna(tabela.loc[linha, coluna]): # Verifica se a observação não é NaN
        pyautogui.write(str(tabela.loc[linha, coluna]))
    pyautogui.press('tab')  # Move para o próximo campo
    pyautogui.click(809, 537)  # Clica no botão de salvar
    pyautogui.click(809, 537)
    time.sleep(2)  # Aguarda um segundo para garantir que o produto foi salvo
    pyautogui.scroll(10000)

