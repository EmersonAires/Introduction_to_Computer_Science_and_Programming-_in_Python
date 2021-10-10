class coelho():
    def __init__(self, peso, idade) -> None:
        self.peso = peso
        self.idade = idade
        self.velocidade = 20
    
    def vel(self):
        print(" The velocity of the habbit is of: {}".format(self.velocidade) )


bil = coelho(1, 3)

# velocidade atribuida no construtor da classe
bil.vel()

#velocidade atribuida fora da classe
bil.velocidade = 40

bil.vel()

# criação de atributos fora da classe
bil.name = "bil"

print(bil.name)