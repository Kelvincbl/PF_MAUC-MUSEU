# 🎨 Museu de Arte UFC (MAUC)

Este projeto simula a gestão de um museu utilizando os conceitos da **Programação Orientada a Objetos (POO)** em Python. Ele inclui a administração de exposições, obras de arte, funcionários e visitantes, proporcionando uma experiência realista de como um museu pode ser gerenciado digitalmente.

---

## 🏛️ Sobre o Projeto

O **Museu de Arte UFC (MAUC)** é um sistema desenvolvido para simular a organização e funcionamento de um museu, permitindo:

- **Gerenciamento de Exposições:** Criação e listagem de exposições com suas respectivas temáticas e obras de arte.
- **Administração de Obras de Arte:** Registro de diferentes obras, incluindo título, artista e ano de criação.
- **Cadastro de Funcionários:** Diferentes categorias de funcionários (guias, curadores, seguranças e administradores) com funções distintas.
- **Interação com Visitantes:** Cadastro de visitantes para representar o público do museu.
- **Aplicação dos princípios da POO:** O projeto implementa os conceitos fundamentais da Programação Orientada a Objetos, tornando o código modular e escalável.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3+
- **Paradigma:** Programação Orientada a Objetos (POO)
- **Estrutura Modular:** Cada classe é representada em um arquivo separado para melhor organização e reutilização do código.

---

## 📂 Estrutura do Projeto

```
📁 mauc_projeto
│── 📄 main.py            # Arquivo principal
│── 📄 museu.py           # Classe Museu
│── 📄 exposicao.py       # Classe Exposicao
│── 📄 obra_de_arte.py    # Classe ObraDeArte
│── 📄 funcionario.py     # Classe base Funcionario
│── 📄 guia.py           # Subclasse Guia
│── 📄 curador.py        # Subclasse Curador
│── 📄 seguranca.py      # Subclasse Segurança
│── 📄 administrador.py  # Subclasse Administrador
│── 📄 visitante.py      # Classe Visitante
└── 📄 README.md         # Documentação do projeto
```

Cada classe possui seus métodos e atributos específicos para modelar um museu de maneira realista.

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório** (se necessário):

```sh
$ git clone https://github.com/seu-usuario/mauc_projeto.git
$ cd mauc_projeto
```

2. **Execute o arquivo principal:**

```sh
$ python main.py
```

---

## 🧩 Explicação das Classes e POO

### 🔹 **Encapsulamento**

- Os atributos das classes são **privados** (`__atributo`) e acessados por métodos `get` e `set`, garantindo segurança e integridade dos dados.

### 🔹 **Herança**

- `Guia`, `Curador`, `Segurança` e `Administrador` **herdam** de `Funcionario`, reutilizando atributos e métodos comuns a todos os funcionários do museu.

### 🔹 **Polimorfismo**

- O método `descrever_funcao()` é **sobrescrito** em cada subclasse, garantindo que cada tipo de funcionário tenha uma descrição específica de sua função.
- Todos os funcionários são armazenados em uma **lista genérica** e iterados sem precisar saber o tipo exato, permitindo flexibilidade e escalabilidade.

### 🔹 **Abstração**

- A classe `Museu` **esconde** detalhes internos e oferece apenas métodos relevantes como `adicionar_exposicao()`, fornecendo uma interface clara para interação.

---

## 📜 Exemplo de Saída

```
Museu: MAUC - Museu de Arte da UFC - Localização: Fortaleza, CE

Exposições e suas obras:
- Arte Cearense (Cultura Nordestina):
  • Pintura Abstrata - Artista Desconhecido (1998)
  • Escultura de Areia - José Lima (2005)
- Arte Moderna Brasileira (Inovação e Expressão):
  • Paisagem Nordestina - Tarsila do Amaral (1929)
  • Abstrato Azul - Cândido Portinari (1951)

Funcionários do museu:
Guia: Carlos é um guia que fala Português.
Curador: Mariana é curadora especializada em Arte Moderna.
Segurança: Rafael trabalha como segurança no turno Noturno.
Administrador: Sofia gerencia a área de Financeiro.

Visitante: Ana, Idade: 22
```

---

## 📝 Autor

Projeto desenvolvido por **[William Kelvin Borges da Costa]**. Caso tenha sugestões ou dúvidas, entre em contato!

