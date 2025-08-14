import random
import time
import os

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_titulo():
    """Mostra o título do jogo"""
    print("=" * 50)
    print("🎮 JOGO DA ADIVINHAÇÃO 🎮")
    print("=" * 50)
    print("Tente adivinhar o número entre 1 e 100!")
    print("Você tem 10 tentativas. Boa sorte! 🍀")
    print("=" * 50)

def jogar_novamente():
    """Pergunta se o jogador quer jogar novamente"""
    while True:
        resposta = input("\n🎯 Quer jogar novamente? (s/n): ").lower().strip()
        if resposta in ['s', 'sim', 'y', 'yes']:
            return True
        elif resposta in ['n', 'não', 'nao', 'no']:
            return False
        else:
            print("❌ Por favor, responda 's' para sim ou 'n' para não!")

def mostrar_dica(numero_secreto, tentativa):
    """Mostra dicas baseadas na tentativa do jogador"""
    if tentativa < numero_secreto:
        print("📈 Dica: O número é MAIOR que", tentativa)
    else:
        print("📉 Dica: O número é MENOR que", tentativa)

def calcular_pontuacao(tentativas_usadas):
    """Calcula a pontuação baseada no número de tentativas"""
    pontuacao_base = 1000
    penalidade_por_tentativa = 50
    pontuacao = pontuacao_base - (tentativas_usadas - 1) * penalidade_por_tentativa
    return max(pontuacao, 100)  # Pontuação mínima de 100

def main():
    """Função principal do jogo"""
    print("🎉 Bem-vindo ao Jogo da Adivinhação! 🎉")
    time.sleep(1)
    
    while True:
        limpar_tela()
        mostrar_titulo()
        
        # Gerar número secreto
        numero_secreto = random.randint(1, 100)
        tentativas_restantes = 10
        tentativas_usadas = 0
        
        print(f"\n🎲 Número secreto gerado! Vamos começar!")
        time.sleep(1)
        
        while tentativas_restantes > 0:
            print(f"\n💡 Tentativas restantes: {tentativas_restantes}")
            
            try:
                tentativa = input("🎯 Digite seu palpite (1-100): ").strip()
                
                # Verificar se é um número válido
                if not tentativa.isdigit():
                    print("❌ Por favor, digite apenas números!")
                    continue
                
                tentativa = int(tentativa)
                
                if tentativa < 1 or tentativa > 100:
                    print("❌ O número deve estar entre 1 e 100!")
                    continue
                
                tentativas_usadas += 1
                tentativas_restantes -= 1
                
                # Verificar se acertou
                if tentativa == numero_secreto:
                    pontuacao = calcular_pontuacao(tentativas_usadas)
                    print("\n" + "🎉" * 20)
                    print("🎉 PARABÉNS! VOCÊ ACERTOU! 🎉")
                    print("🎉" * 20)
                    print(f"🎯 Número secreto: {numero_secreto}")
                    print(f"🎮 Tentativas usadas: {tentativas_usadas}")
                    print(f"🏆 Pontuação: {pontuacao} pontos!")
                    
                    if tentativas_usadas <= 3:
                        print("🌟 INCRÍVEL! Você é um mestre da adivinhação!")
                    elif tentativas_usadas <= 5:
                        print("⭐ Muito bem! Você tem talento para isso!")
                    else:
                        print("👍 Boa jogada! Continue praticando!")
                    
                    break
                
                else:
                    print(f"❌ Ops! {tentativa} não é o número correto!")
                    mostrar_dica(numero_secreto, tentativa)
                    
                    if tentativas_restantes > 0:
                        print(f"💪 Não desista! Ainda há {tentativas_restantes} tentativa(s)!")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Jogo interrompido pelo usuário. Até logo!")
                return
            except Exception as e:
                print(f"❌ Erro inesperado: {e}")
                continue
        
        # Se acabaram as tentativas
        if tentativas_restantes == 0 and tentativa != numero_secreto:
            print("\n" + "💔" * 15)
            print("💔 GAME OVER! 💔")
            print("💔" * 15)
            print(f"🎯 O número secreto era: {numero_secreto}")
            print("😢 Não foi dessa vez, mas não desista!")
            print("💪 Tente novamente e você conseguirá!")
        
        # Perguntar se quer jogar novamente
        if not jogar_novamente():
            print("\n👋 Obrigado por jogar! Até a próxima! 👋")
            print("🎮 Espero que tenha se divertido! 🎮")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Jogo finalizado. Até logo!")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("😔 O jogo encontrou um problema inesperado.")
