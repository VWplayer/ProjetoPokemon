import random 
class Pokemon:
    def __init__(self,nome,especie,tipo,ataque,defesa,hp):
        self._nome = nome
        self._especie = especie
        self._tipo = tipo
        self._ataque = ataque
        self._defesa = defesa
        self._hp = hp
        self._movimento = "Ataque rapido"
class Aquatico(Pokemon):
    def __init__(self,nome,especie,tipo,ataque,defesa,hp,):
     super().__init__(nome,especie,tipo,ataque,defesa,hp)
     self._tipo = "Aquatico"
     self._movimento = "Jato de água"


class Fogo(Pokemon):
    def __init__(self,nome,especie,tipo,ataque,defesa,hp):
     super().__init__(nome,especie,tipo,ataque,defesa,hp)
     self._tipo = "Fogo"
     self._movimento = "Lança Chamas"
    
class Elétrico(Pokemon):
    def __init__(self,nome,especie,tipo,ataque,defesa,hp):
     super().__init__(nome,especie,tipo,ataque,defesa,hp)
     self._tipo = "Eletrico"
     self._movimento = "Raio do trovão"

class Grama(Pokemon):
    def __init__(self,nome,especie,tipo,ataque,defesa,hp):
     super().__init__(nome,especie,tipo,ataque,defesa,hp)
     self._tipo = "Grama"
     self._movimento = "Folhas navalha"

class Treinador:
    def __init__(self,nome,pokemons):
        self._nome = nome
        self._pokemons = pokemons
    def escolherPokemon(self):
        return random.choice(self._pokemons)

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

class Inimigo(Treinador):
    def __init__(self,nome,pokemons):
        super().__init__(nome,pokemons)

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
    
    elif (p1tipo is "Eletrico" and p2tipo is "Agua"):
        print(f"O vencedor foi {p1._especie} do treinador {p1._nome}")
    elif (p1tipo is "Agua" and p2tipo is "Eletrico"):
        print(f"O vencedor foi {p2._especie} do treinador {p2._nome}")

    elif (p1tipo is "Eletrico" and p2tipo is "Grama"):
        print(f"O vencedor foi {p1._especie} do treinador {p1._nome}")
    elif (p1tipo is "Grama" and p2tipo is "Eletrico"):
        print(f"O vencedor foi {p2._especie} do treinador {p2._nome}")
    else:
        print("Os pokemons são de mesmo tipo a batalha deu empate")
          
PokemonsDisp = [
Fogo("Ash", "Charmander", "Fogo", 50,50,50),
Grama("Jessy", "bulbassauro", "Grama", 50,50,50),
Aquatico("James", "Tentacruel", "Aquatico", 50,50,50),
Elétrico("Wendel", "Electabuzz", "Eletrico", 50,50,50)
]
jogador = Jogador("Wendel",[PokemonsDisp[0],PokemonsDisp[1],PokemonsDisp[2],PokemonsDisp[3]])
inimigo = Inimigo("James", [PokemonsDisp])

BatalhaPokemon(jogador, inimigo)