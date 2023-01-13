import random 

class Pokemon:
    def __init__(self,nome,especie,tipo):
        self._nome = nome
        self._especie = especie
        self._tipo = tipo
        self._movimento = "Ataque rapido"
class Aquatico(Pokemon):
    def __init__(self,nome,especie,tipo):
     super().__init__(nome,especie,tipo)
     self._tipo = "Aquatico"
     self._movimento = "Jato de água"


class Fogo(Pokemon):
    def __init__(self,nome,especie,tipo):
     super().__init__(nome,especie,tipo)
     self._tipo = "Fogo"
     self._movimento = "Lança Chamas"
    
class Elétrico(Pokemon):
    def __init__(self,nome,especie,tipo):
     super().__init__(nome,especie,tipo)
     self._tipo = "Eletrico"
     self._movimento = "Raio do trovão"

class Grama(Pokemon):
    def __init__(self,nome,especie,tipo):
     super().__init__(nome,especie,tipo)
     self._tipo = "Grama"
     self._movimento = "Folhas navalha"

class Treinador:
    def __init__(self,nome,pokemons):
        self._nome = nome
        self._pokemons = pokemons

class Jogador(Treinador):
    def __init__(self,nome,pokemons):
        super().__init__(nome,pokemons) 

    def escolherPokemon(self):
        while True:
            print(f"Escolha seu pokemon: ")

            for i in range(len(self._pokemons)):
                print(f"{i+1}. {self._pokemons[i]._especie}")

            pokemonEscolhido = input("Digite o número do pokemon escolhido: ")

            return self._pokemons[int(pokemonEscolhido)-1] 
            
            if (pokemonEscolhido.isnumeric()):
                if (int(pokemonEscolhido) <= len(self._pokemons)):
                    return self._pokemons[pokemonEscolhido]
                else:
                    print("Você escreveu um número maior do que o disponível.")
            else: 
                print("Você escreveu um caractere inválido")
    def listarPokemons(self):
        print(f"seus pokemons são")
        for i in range(len(self._pokemons)) :
            print(f"{i+1} - {self._pokemons[i]._especie}")

    def capturarPokemon(self, pokemonCapturado):    
        self._pokemons.append(pokemonCapturado)
        print(f"Você capturou o {pokemonCapturado._especie}")

class Inimigo(Treinador):
    def __init__(self,nome,pokemons):
        super().__init__(nome,pokemons)
    def escolherPokemon(self):
        return random.choice(self._pokemons)

def BatalhaPokemon(treinador1, treinador2):

    p1 = treinador1.escolherPokemon()
    p2 = treinador2.escolherPokemon()

    p1tipo = p1._tipo
    p2tipo = p2._tipo

    print(f"{p1._nome} atacou com o {p1._especie} usando a habilidade {p1._movimento}")

    print(f"{p2._nome} atacou com o {p2._especie} usando a habilidade {p2._movimento}")

    if (p1tipo is "Aquatico" and p2tipo is "Fogo"):
        print(f"O vencedor foi {p1._especie} do treinador {p1._nome}")
    elif (p1tipo is "Fogo" and p2tipo is "Aquatico"):
        print(f"O vencedor foi {p2._especie} do treinador {p2._nome}")
        
    elif (p1tipo is "Aquatico" and p2tipo is "Grama"):
        print(f"O vencedor foi {p2._especie} do treinador {p2._nome}")
    elif (p1tipo is "Grama" and p2tipo is "Aquatico"):
        print(f"O vencedor foi {p1._especie} do treinador {p1._nome}")
    
    elif (p1tipo is "Fogo" and p2tipo is "Grama"):
        print(f"O vencedor foi {p1._especie} do treinador {p1._nome}")
    elif (p1tipo is "Grama" and p2tipo is "Fogo"):
        print(f"O vencedor foi {p2._especie} do treinador {p2._nome}")

    elif (p1tipo is "Fogo" and p2tipo is "Eletrico"):
        print(f"O vencedor foi {p2._especie} do treinador {p2._nome}")
    elif (p1tipo is "Eletrico" and p2tipo is "Fogo"):
        print(f"O vencedor foi {p1._especie} do treinador {p1._nome}")
    
    elif (p1tipo is "Eletrico" and p2tipo is "Aquatico"):
        print(f"O vencedor foi {p1._especie} do treinador {p1._nome}")
    elif (p1tipo is "Aquatico" and p2tipo is "Eletrico"):
        print(f"O vencedor foi {p2._especie} do treinador {p2._nome}")

    elif (p1tipo is "Eletrico" and p2tipo is "Grama"):
        print(f"O vencedor foi {p1._especie} do treinador {p1._nome}")
    elif (p1tipo is "Grama" and p2tipo is "Eletrico"):
        print(f"O vencedor foi {p2._especie} do treinador {p2._nome}")
    else:
        print("Os pokemons são de mesmo tipo a batalha deu empate")
          
PokemonsDisp = [
Fogo("Ash", "Charmander", "Fogo"),
Grama("Jessy", "bulbassauro", "Grama"),
Aquatico("James", "Tentacruel", "Aquatico"),
Elétrico("Wendel", "Electabuzz", "Eletrico")
]

nomeJogador = input("Digite seu nome: ")

print("Escolha seu Pokemon inicial: ")

for i in range(4):
    print(f"{i+1}. {PokemonsDisp[i]._especie}")

pokemonInicial = PokemonsDisp[int(input("Digite o pokemon escolhido: "))-1]

print(f"O pokemon escolhido foi o {pokemonInicial._especie}")

jogador = Jogador(nomeJogador, [pokemonInicial])
inimigo = Inimigo("James", PokemonsDisp)

while True:

    print("""
    Escolha o que você quer fazer:
    1. Ver seus Pokemons
    2. Capturar um novo Pokemon
    3. Batalhar contra um oponente
    0. Sair do jogo
    """)

    menu = input("Digite a opção escolhida:")

    if menu =="0":
        print("Você saiu do jogo.")
        break
    elif menu=="1":
        jogador.listarPokemons()
    elif menu=="2":
        print("Escolha um pokemon para capturar: ")

        for i in range(len(PokemonsDisp)):
            print(f"{i+1}. {PokemonsDisp[i]._especie}")
        
        capturado = PokemonsDisp[int(input("Digite o pokemon escolhido: "))-1]
        jogador.capturarPokemon(capturado)
    elif menu=="3":
        BatalhaPokemon(jogador,inimigo)
    else:
        print("Você digitou algo inválido, tente novamente.")
    
