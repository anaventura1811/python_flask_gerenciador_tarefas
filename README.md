# Task Manager - Flask CRUD

## Introdução

Bem-vindo(a) ao repositório do **Task Manager**, um projeto simples de CRUD (Create, Read, Update, Delete) desenvolvido em Flask. Este projeto foi criado como parte dos meus estudos sobre Python e desenvolvimento web na **Rocketseat**, com o objetivo de consolidar conhecimentos em backend e manipulação de dados. 

## Sobre o Projeto

O **Task Manager** permite que o usuário crie, visualize, edite e delete tarefas. Este CRUD básico é apenas um exemplo, criado para fixar os conceitos de APIs REST, bem como uso do **Flask**. Inclui também testes unitários dos endpoints com a lib **PyTest**. Portanto, pode servir como referência e ponto de partida para quem deseja entender como construir uma aplicação completa e funcional em Flask, explorando a manipulação de dados, as rotas RESTful e a criação de testes unitários de forma prática.

### Funcionalidades

- **Criar Tarefa**: Permite ao usuário adicionar uma nova tarefa com um título e descrição.
- **Listar Tarefas**: Exibe todas as tarefas registradas, organizadas para fácil visualização.
- **Listar Tarefa**: Exibe uma tarefa registrada, com base no id passado pelo usuário no endpoint.
- **Editar Tarefa**: Possibilita a edição de informações de uma tarefa existente.
- **Excluir Tarefa**: Permite a remoção de uma tarefa da lista.

### Estrutura da Aplicação

A aplicação foi organizada em rotas RESTful, conforme as boas práticas do desenvolvimento web com Flask. Cada operação do CRUD possui uma rota dedicada:

- **GET /tasks**: Visualiza a lista de tarefas.
- **GET /tasks/<id>**: Visualiza uma tarefa.
- **POST /tasks**: Adiciona uma nova tarefa.
- **PUT /tasks/<id>**: Edita uma tarefa existente.
- **DELETE /tasks/<id>**: Exclui uma tarefa específica.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Flask**: Framework web utilizado para criar a API.
- **PyTest**: Lib para criação e execução de testes unitários na API.

## Como Rodar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/anaventura1811/python_flask_gerenciador_tarefas.git
   
2. Navegue até o diretório do projeto:
   ```bash
   cd python_flask_gerenciador_tarefas

4. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate

6. Instale as dependências:
    ```bash
    pip install -r requirements.txt

7. Execute a aplicação:
    ```bash
    flask run

    # Ou alternativamente, execute na raiz do projeto:
    python app.py

Acesse a aplicação no navegador pelo endereço: **http://127.0.0.1:5000/tasks**.


