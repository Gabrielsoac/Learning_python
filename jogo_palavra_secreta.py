#JOGO PALAVRA SECRETA

import os 

def finalizar_game():
    finalizar = input('Gostaria de chutar agora? [Sim] ou [Nao]?: ').lower()
    
    if finalizar == 'sim':
        return True
    elif finalizar == 'nao':
        return False
    elif finalizar != 'sim' or finalizar != 'nao':
         finalizar = finalizar_game()
         return finalizar



palavra = 'liquidificador'
tentativas = 0
finalizar = False
letras_acertadas = ''


while True:
        
        os.system('cls')
        
        #enunciado
        print(f'''A palavra secreta da vez possui {len(palavra)} letras ''')

        #primeira parte, chutes
        tentativas += 1
        chute = input('''Digite uma letra para a palavra secreta, 
        se a letra estiver na palavra, será exibida: ''').lower()

        if not chute:
                print('Você não digitou nada!')
                continue
        
        if len(chute) > 1:
             print('Digite apenas uma letra por vez!')
             continue
        
        if chute in palavra:
                print(chute)
                print(f'A letra "{chute}" aparece {palavra.count(chute)}x na palavra secreta')
        else:
                print(f'{chute} não está na palavra secreta')

        if chute in palavra:
             letras_acertadas += chute

        palavra_formada = ''
        for letra_secreta in palavra:
             if letra_secreta in letras_acertadas:
                  palavra_formada += letra_secreta
             else:
                  palavra_formada += '*'
        
        print(palavra_formada)
    
        
        #segunda parte, tentativas
        if tentativas == 20:
            finalizar = True
            ultimo_chute = input('Digite o seu chute para a palavra: ').lower()
            if ultimo_chute == palavra:
                print('Parabéns, você venceu!')
                print(f'A palavra secreta é {palavra}')
                print(f'Número de tentativas = {tentativas}')
                break
            else:
                print('Você foi derrotado!')
                print(f'A palavra secreta é {palavra}')
                print(f'Número de tentativas = {tentativas}')
                break

        elif tentativas < 20:
            print(f'Número de tentativas = {tentativas}')
            print('Ao chegar na tentiva número 20, não poderá continuar!')
            finalizar = finalizar_game() #terceira parte, continuar ou desistir

            if finalizar == False:
              continue
            elif finalizar == True:
                ultimo_chute = input('Digite o seu chute para a palavra: ').lower()
                if ultimo_chute == palavra:
                    print('Parabéns, você venceu!')
                    print(f'A palavra secreta é {palavra}')
                    print(f'Número de tentativas = {tentativas}')
                    break
                else:
                    print('Você foi derrotado!')
                    print(f'A palavra secreta é {palavra}')
                    print(f'Número de tentativas = {tentativas}')
                    break
        
        
        

    