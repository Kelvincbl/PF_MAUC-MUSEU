# PF_MAUC-MUSEU

# 🎨 Museu de Arte UFC (MAUC)

Este projeto simula a gestão de um museu utilizando os conceitos da **Programação Orientada a Objetos (POO)** em Python. Ele inclui a administração de exposições, obras de arte, funcionários e visitantes.

---

## 🏛️ Sobre o Projeto

O **Museu de Arte UFC (MAUC)** é um sistema que:

- Gerencia exposições e suas obras de arte.
- Cadastra funcionários, incluindo guias, curadores, seguranças e administradores.
- Permite a criação e listagem de visitantes.
- Aplica os princípios de **Encapsulamento, Herança, Polimorfismo e Abstração**.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3+
- **Paradigma:** Programação Orientada a Objetos (POO)

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

- Os atributos das classes são **privados** (`__atributo`) e acessados por métodos `get` e `set`.

### 🔹 **Herança**

- `Guia`, `Curador`, `Segurança` e `Administrador` **herdam** de `Funcionario`.

### 🔹 **Polimorfismo**

- O método `descrever_funcao()` é **sobrescrito** em cada subclasse.
- Todos os funcionários são armazenados em uma **lista genérica** e iterados sem precisar saber o tipo exato.

### 🔹 **Abstração**

- A classe `Museu` **esconde** detalhes internos e oferece apenas métodos relevantes como `adicionar_exposicao()`.

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

## 🔥 Possíveis Melhorias

- Adicionar um sistema de agendamento de visitas.
- Implementar um banco de dados para armazenar as informações.

---

## 📝 Autor

Projeto desenvolvido por **[William Kelvin Borges da Costa]**.

