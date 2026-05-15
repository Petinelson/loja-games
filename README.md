# 🎮 GameMaster — Sistema de Gerenciamento de Jogos e Plataformas

> Projeto educacional desenvolvido com **Python + Flask**, demonstrando os fundamentos do desenvolvimento web backend com persistência de dados em arquivos de texto.

---

## 📋 Sobre o Projeto

O **GameMaster** é uma aplicação web CRUD completa para gerenciar um catálogo de jogos e plataformas de videogame. O projeto foi desenvolvido com fins **educacionais**, com foco em apresentar de forma simples e direta os conceitos de rotas HTTP, formulários, manipulação de arquivos e renderização de templates com Flask.

A ideia central é simular o backend de uma loja de videogames, onde é possível cadastrar plataformas (como PlayStation, Xbox, Nintendo) e associar jogos a elas.
[Teste o projeto](https://petigames.onrender.com)

---

## ✨ Funcionalidades

### 🕹️ Gerenciamento de Plataformas
- **Cadastrar** plataforma com nome, fabricante e imagem (upload de arquivo)
- **Listar** todas as plataformas cadastradas com visualização da imagem
- **Editar** nome e fabricante de uma plataforma existente
- **Excluir** plataforma (remove também a imagem associada do servidor)

### 🎯 Gerenciamento de Jogos
- **Cadastrar** jogo com título, gênero, data de lançamento e plataforma associada
- **Listar** todos os jogos cadastrados
- **Editar** informações de um jogo existente
- **Excluir** jogo do catálogo

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Função |
|---|---|---|
| Python | 3.x | Linguagem principal |
| Flask | 3.1.0 | Framework web (servidor, rotas, templates) |
| Jinja2 | 3.1.5 | Motor de templates HTML |
| Werkzeug | 3.1.3 | Utilitários WSGI (usado internamente pelo Flask) |
| HTML5/CSS3 | — | Interface do usuário |

### Persistência de Dados
Os dados são armazenados em **arquivos `.txt`** com campos separados por `;` (sem banco de dados), o que simplifica a compreensão do fluxo de leitura e escrita de dados para fins didáticos.

```
# Exemplo: models/plataformas.txt
uuid;nome;fabricante;caminho_da_imagem

# Exemplo: models/jogos.txt
uuid;titulo;genero;data_lancamento;cod_plataforma
```

---

## 📁 Estrutura do Projeto

```
gamemaster/
│
├── run.py                    # Arquivo principal — rotas e lógica da aplicação
│
├── templates/                # Templates HTML (Jinja2)
│   ├── index.html
│   ├── cadastro_plataformas.html
│   ├── consulta_plataformas.html
│   ├── editar_plataforma.html
│   ├── cadastro_jogos.html
│   ├── consulta_jogos.html
│   └── editar_jogo.html
│
├── static/
│   ├── styles/
│   │   └── estilo.css        # Estilos da aplicação
│   └── assets/               # Imagens das plataformas e ícones da UI
│
├── models/
│   ├── plataformas.txt       # "Banco de dados" de plataformas
│   └── jogos.txt             # "Banco de dados" de jogos
│
└── requirements.txt          # Dependências do projeto
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.8 ou superior instalado
- `pip` disponível no terminal

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/gamemaster.git
cd gamemaster
```

**2. Crie e ative um ambiente virtual** *(recomendado)*
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python -m venv venv
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Crie a estrutura de pastas necessária**
```bash
mkdir -p models static/assets
touch models/plataformas.txt models/jogos.txt
```

**5. Execute a aplicação**
```bash
python run.py
```

**6. Acesse no navegador**
```
http://localhost:5000
```

---

## 🗺️ Rotas da Aplicação

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Página inicial |
| GET/POST | `/cadastro_plataformas` | Formulário de cadastro de plataforma |
| GET | `/consulta_plataformas` | Lista todas as plataformas |
| GET/POST | `/editar_plataforma?linha=N` | Edita a plataforma da linha N |
| GET | `/excluir_plataforma?linha=N` | Exclui a plataforma da linha N |
| GET/POST | `/cadastro_jogos` | Formulário de cadastro de jogo |
| GET | `/consulta_jogos` | Lista todos os jogos |
| GET/POST | `/editar_jogo?linha=N` | Edita o jogo da linha N |
| GET | `/excluir_jogo?linha=N` | Exclui o jogo da linha N |

---

## 📚 Conceitos Abordados

Este projeto é ideal para estudantes que estão aprendendo:

- ✅ **Rotas HTTP** com Flask (`GET` e `POST`)
- ✅ **Templates dinâmicos** com Jinja2 (laços, condicionais, variáveis)
- ✅ **Formulários HTML** e captura de dados com `request.form`
- ✅ **Upload de arquivos** com `request.files`
- ✅ **Leitura e escrita de arquivos** em Python
- ✅ **Redirecionamento** com `redirect()`
- ✅ **Identificadores únicos** com `uuid`
- ✅ **Separação de responsabilidades**: rotas, templates e dados
- ✅ **Operações CRUD**: Create, Read, Update e Delete

---

## ⚠️ Limitações Conhecidas (e Oportunidades de Melhoria)

Por ser um projeto didático, algumas práticas foram simplificadas intencionalmente. Possíveis evoluções:

- [ ] Substituir os arquivos `.txt` por um banco de dados (SQLite, PostgreSQL)
- [ ] Adicionar validação de formulários no backend
- [ ] Implementar tratamento de erros (arquivo não encontrado, campo vazio)
- [ ] Adicionar autenticação de usuário
- [ ] Migrar para um ORM como SQLAlchemy
- [ ] Exibir o nome da plataforma no lugar do UUID na consulta de jogos

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usá-lo, modificá-lo e distribuí-lo para fins educacionais.

---

> Desenvolvido com 🎮 e Python para fins de aprendizado.
