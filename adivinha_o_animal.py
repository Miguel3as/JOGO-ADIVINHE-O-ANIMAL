import json
import os
import random

# Dados dos 14 animais e suas dicas
animais = {
    "leão": {
        "dicas": [
            "É conhecido como o rei da selva.",
            "Vive em grupos chamados de 'coalizões'.",
            "Possui uma juba característica (no caso dos machos)."
        ]
    },
    "girafa": {
        "dicas": [
            "É o animal mais alto do mundo.",
            "Tem um pescoço muito longo.",
            "Possui manchas características em seu corpo."
        ]
    },
    "elefante": {
        "dicas": [
            "É o maior animal terrestre.",
            "Possui uma tromba longa e flexível.",
            "Tem grandes orelhas que ajudam a regular sua temperatura."
        ]
    },
    "pinguim": {
        "dicas": [
            "É uma ave que não voa.",
            "Vive principalmente no hemisfério sul.",
            "Excelente nadador e se alimenta no mar."
        ]
    },
    "cobra": {
        "dicas": [
            "Réptil sem pernas.",
            "Algumas espécies são venenosas.",
            "Troca de pele periodicamente."
        ]
    },
    "tigre": {
        "dicas": [
            "Maior felino do mundo.",
            "Possui listras que são únicas em cada indivíduo.",
            "Excelente nadador ao contrário de outros felinos."
        ]
    },
    "macaco": {
        "dicas": [
            "Primata inteligente com cauda longa.",
            "Vive em grupos sociais complexos.",
            "Alimenta-se principalmente de frutas e vegetais."
        ]
    },
    "zebra": {
        "dicas": [
            "Parecida com um cavalo com listras.",
            "Cada padrão de listras é único como uma impressão digital.",
            "Vive em savanas africanas."
        ]
    },
    "hipopótamo": {
        "dicas": [
            "Grande mamífero que passa muito tempo na água.",
            "Considerado um dos animais mais perigosos da África.",
            "Produz um suor vermelho que age como protetor solar."
        ]
    },
    "rinoceronte": {
        "dicas": [
            "Grande mamífero com chifres característicos.",
            "Tem pele grossa e resistente.",
            "Está em perigo de extinção devido à caça por seus chifres."
        ]
    },
    "cachorro caramelo": {
        "dicas": [
            "É amado pelo povo brasileiro.",
            "Tem pelagem na cor caramelo.",
            "Conhecido por ser muito amigável e companheiro."
        ]
    },
    "papagaio": {
        "dicas": [
            "Ave conhecida por imitar a voz humana.",
            "Possui penas coloridas e bico curvo.",
            "Muito inteligente e social."
        ]
    },
    "arara": {
        "dicas": [
            "Ave grande com penas coloridas vibrantes.",
            "Tem um bico forte e cauda longa.",
            "Vive principalmente em florestas tropicais."
        ]
    },
    "gato": {
        "dicas": [
            "Animal doméstico muito popular.",
            "Conhecido por sua independência e agilidade.",
            "Gosta de caçar pequenos animais e brincar com bolinhas."
        ]
    }
}

# Sistema de pontuação e histórico
historico_jogadores = []

def carregar_historico():
    global historico_jogadores
    if os.path.exists('historico.json'):
        with open('historico.json', 'r') as f:
            historico_jogadores = json.load(f)

def salvar_historico():
    with open('historico.json', 'w') as f:
        json.dump(historico_jogadores, f)

def mostrar_menu_continuar():
    print("\nDeseja continuar jogando?")
    print("(1) Sim")
    print("(2) Não - Ver meu resultado e sair")
    
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao in [1, 2]:
                return opcao == 1
            print("Por favor, digite 1 para continuar ou 2 para sair.")
        except ValueError:
            print("Entrada inválida. Digite 1 ou 2.")

def mostrar_historico(jogador_atual=None):
    print("\n=== HISTÓRICO DE JOGADORES ===")
    
    # Ordenar por pontuação (maior primeiro)
    historico_ordenado = sorted(historico_jogadores, key=lambda x: x['pontuacao'], reverse=True)
    
    if not historico_ordenado:
        print("Nenhum registro encontrado.")
        return
    
    # Encontrar posição do jogador atual
    posicao_jogador = None
    if jogador_atual:
        for i, jogador in enumerate(historico_ordenado, 1):
            if jogador['nome'].lower() == jogador_atual['nome'].lower() and jogador['pontuacao'] == jogador_atual['pontuacao']:
                posicao_jogador = i
                break
    
    # Mostrar histórico completo
    for i, jogador in enumerate(historico_ordenado, 1):
        marcador = ">>> " if posicao_jogador and i == posicao_jogador else "    "
        print(f"{marcador}{i}. {jogador['nome']}: {jogador['pontuacao']} pontos")
    
    if posicao_jogador:
        print(f"\nVocê está na posição {posicao_jogador} do ranking!")

def selecionar_animal_aleatorio():
    return random.choice(list(animais.keys()))

def jogo_adivinhacao():
    carregar_historico()
    
    print("=== JOGO DE ADIVINHAÇÃO DE ANIMAIS ===")
    nome_jogador = input("Digite seu nome: ").strip()  # Remove espaços extras
    pontuacao_total = 0
    
    # Verifica se o jogador já existe no histórico (comparação case-insensitive)
    jogador_existente = None
    for jogador in historico_jogadores:
        if jogador['nome'].lower() == nome_jogador.lower():
            jogador_existente = jogador
            pontuacao_total = jogador['pontuacao']
            print(f"\nBem-vindo de volta, {nome_jogador}! Sua pontuação atual é {pontuacao_total} pontos.")
            break
    
    continuar_jogando = True
    
    while continuar_jogando:
        # Seleciona um animal aleatório
        animal = selecionar_animal_aleatorio()
        dicas = animais[animal]['dicas']
        
        print(f"\nTente adivinhar o animal! Você tem 3 tentativas.")
        print(f"Dica inicial: {dicas[0]}")
        pontuacao_rodada = 10  # Pontos máximos por rodada
        
        for tentativa in range(3):
            palpite = input(f"\nTentativa {tentativa + 1}: ").lower()
            
            if palpite == animal:
                print(f"\nParabéns! Você acertou. O animal é {animal}.")
                print(f"Você ganhou {pontuacao_rodada} pontos nesta rodada!")
                pontuacao_total += pontuacao_rodada
                break
            else:
                if tentativa < 2:  # Mostra dicas apenas nas primeiras 2 tentativas
                    print(f"Dica adicional: {dicas[tentativa+1]}")
                pontuacao_rodada -= 3  # Perde 3 pontos por erro
        
        else:  # Se esgotou todas as tentativas
            print(f"\nSuas tentativas acabaram! O animal era {animal}.")
            if pontuacao_rodada < 0:
                pontuacao_rodada = 0
            print(f"Você ganhou {pontuacao_rodada} pontos nesta rodada.")
            pontuacao_total += pontuacao_rodada
        
        continuar_jogando = mostrar_menu_continuar()
    
    # Atualiza o histórico
    if jogador_existente:
        # Atualiza a pontuação do jogador existente
        jogador_existente['pontuacao'] = pontuacao_total
    else:
        # Adiciona novo jogador apenas se não existir
        novo_jogador = {
            'nome': nome_jogador,
            'pontuacao': pontuacao_total
        }
        historico_jogadores.append(novo_jogador)
    
    salvar_historico()
    
    # Mostra resultados finais
    print(f"\n=== FIM DE JOGO ===")
    print(f"Pontuação total de {nome_jogador}: {pontuacao_total} pontos")
    mostrar_historico({'nome': nome_jogador, 'pontuacao': pontuacao_total})

# Iniciar o jogo
if __name__ == "__main__":
    jogo_adivinhacao()