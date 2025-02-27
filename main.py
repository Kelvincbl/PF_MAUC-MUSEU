from museu import Museu
from exposicao import Exposicao
from obra_de_arte import ObraDeArte
from guia import Guia
from curador import Curador
from seguranca import Seguranca
from administrador import Administrador
from visitante import Visitante

# Criando o Museu
mauc = Museu("MAUC - Museu de Arte da UFC", "Fortaleza, CE")

# Criando Exposições
exposicao1 = Exposicao("Arte Cearense", "Cultura Nordestina")
exposicao2 = Exposicao("Arte moderna Brasileira", "Inovação e Expressão")

# Criando Obras de Arte
obra1 = ObraDeArte("Pintura Abstrata", "Artista Desconhecido", 1998)
obra2 = ObraDeArte("Escultura de Areia", "José Lima", 2005)
obra3 = ObraDeArte("Paisagem Nordestina", "Tarsila do Amaral", 1929)
obra4 = ObraDeArte("Abstrato Azul", "Cândido Portinari", 1951)


# Adicionando obras à exposição
exposicao1.adicionar_obra(obra1)
exposicao1.adicionar_obra(obra2)
exposicao2.adicionar_obra(obra3)
exposicao2.adicionar_obra(obra4)

# Adicionando exposição ao museu
mauc.adicionar_exposicao(exposicao1)
mauc.adicionar_exposicao(exposicao2)

# Criando funcionários (Guias, Curadores, Seguranças e Administradores)
guia1 = Guia("Carlos", "Português")
guia2 = Guia("Fernanda", "Inglês")
curador1 = Curador("Mariana", "Arte Moderna")
curador2 = Curador("Amanda", "Arte Clássica")
seguranca1 = Seguranca("Rafael", "Noturno")
seguranca2 = Seguranca("João", "Diurno")
admin1 = Administrador("Sofia", "Financeiro")
admin2 = Administrador("Roberto", "Recursos Humanos")


# Lista polimórfica de funcionários
funcionarios = [guia1, guia2, curador1, curador2, seguranca1, seguranca2, admin1, admin2,]

# Criando um Visitante
visitante1 = Visitante("Ana", 22)
visitante2 = Visitante("Kelvin", 21)

# Exibindo informações do museu
print(f"Museu: {mauc.get_nome()} - Localização: {mauc.get_localizacao()}")
print("Exposições disponíveis:", mauc.listar_exposicoes())
print(f"Obras na exposição {exposicao1.get_nome()}: {exposicao1.listar_obras()}")
print(f"Obras na exposição {exposicao2.get_nome()}: {exposicao2.listar_obras()}")


# Usando polimorfismo para listar funcionários
print("\nFuncionários do museu:")
for func in funcionarios:
    print(func.descrever_funcao())  # Chamando o método polimórfico

# Exibindo informações do visitante
print(f"\nVisitante: {visitante1.get_nome()}, Idade: {visitante1.get_idade()}")
print(f"\nVisitante: {visitante2.get_nome()}, Idade: {visitante2.get_idade()}")
