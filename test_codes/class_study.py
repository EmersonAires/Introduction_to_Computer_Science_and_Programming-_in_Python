class carro():
    message = "I am a car"
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    def __str__(self) -> str:
        return "Modelo: {}, Cor: {}, Ano: {}".format(self.modelo, self.cor, self.ano)
    
    def __eq__(self, other_car) -> bool:

        return self.ano == other_car.ano
    
    def __add__(self, other_car):

        ano1= int(self.ano)
        ano2= int(other_car.ano)
        soma= ano1 + ano2
        
        return soma
    


chapolim = carro("Strada", "Vermelho", "2010")

barao = carro("gol", "vermelho", "2010")


print("O ano do Chapolim é igual ao ano do barão?", chapolim == barao)

print(chapolim + barao)

""" print(chapolim.message)
print(chapolim.modelo)
print(chapolim.cor)
print(chapolim.ano) """

# Chama o método especial da classe (__str__) e executa a implementação
print("características -->", chapolim)

print("-------------------------")

# Tipo do objeto
print("Tipo (chapolim) -->", type(chapolim))

print("-------------------------")

# Checa se o objeto é uma instância da classe
print("É instância da classe? -->", isinstance(chapolim, carro))

print("-------------------------")

print("Tipo da classe carro -->", type(carro))

print("-------------------------")

print("Imprime a classe carro -->", carro)

print("-------------------------")
print(type(chapolim.modelo))

