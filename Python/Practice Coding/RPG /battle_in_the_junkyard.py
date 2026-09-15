print("===== Batalha no Lixão =====")
nome = input("Digite o nome do seu personagem: ")

life = 70
life_bot = 61
pocoes = 1

print(f"\n Ola {nome}, você está perdido no lixão, e encontrou um Lixo Bot!\n")

# Loop para até 5 rodadas
for rodada in range(1, 6):
    print(f"\n--- Rodada {rodada} ---")
    print(f"Vida do {nome}: {life}")
    print(f"Vida do Lixo Bot: {life_bot}")
    
    acao = input("Escolha sua ação ([1] atacar, [2] usar poção, [3] fugir): ").strip()
    
    if acao == "1":
        dano = 25
        life_bot -= dano
        print(f"\nVocê atacou o Lixo Bot e causou {dano} de dano!")
        
        # O robô só contra-ataca se ainda estiver vivo
        if life_bot > 0:
            life -= 15
            print(f"O Lixo Bot atacou você. Sua vida agora é {life}.")
            
    elif acao == "2":
        if pocoes > 0:
            life += 15
            pocoes -= 1
            print(f"\nVocê recuperou 15 pontos de vida. Sua vida agora é {life}. Poções restantes: {pocoes}.")
            
            # O robô ataca você enquanto você usa a poção
            life -= 15
            print(f"O Lixo Bot aproveitou seu turno e atacou! Sua vida agora é {life}.")
        else:
            print("\nVocê não tem poções restantes!")
            continue  # Volta para o início da rodada sem gastar o turno
            
    elif acao == "3":
        print(f"\n{nome} fugiu da batalha como um covarde!")
        break
        
    else:
        print("\nAção inválida! Você perdeu a vez.")
        if life_bot > 0:
            life -= 15
            print(f"O Lixo Bot atacou você. Sua vida agora é {life}.")

    # Verifica condições de fim de jogo dentro do loop para encerrar imediatamente
    if life_bot <= 0:
        print(f"\n🏆 YOU WIN, {nome}! Você derrotou o Lixo Bot!")
        break
    elif life <= 0:
        print(f"\n💀 GAME OVER, {nome}! Você foi derrotado pelo Lixo Bot!")
        break
else:
    # Se o loop terminar as 5 rodadas sem ninguém morrer
    print("\n⏱️ O tempo acabou! A batalha terminou em empate.")
