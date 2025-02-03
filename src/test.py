from src.controllers.gestao import *

while True:
    print ('Menu\n')
    print (f' 1. Inserir novo produto\n 2. Adicinar produto\n 3. Remover uma quantidade \n 4. Remover produto do estoque\n 5. Ver valor total do estoque\n 6. Ver valor total do produto \n 7. Ver quantidade do produto \n 8. Sair do programa')
    opcao = int(input('Qual opçao'))

    if opcao == 1:
        inserir()
    if opcao == 2:
        adicionar()
    if opcao == 8:
        break

