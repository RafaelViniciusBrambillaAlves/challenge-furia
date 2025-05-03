# 🕹️ Know Your Fan - FURIA Esports | Data Experience Project

Este projeto foi desenvolvido como parte de um desafio para a vaga de **Assistente de Engenharia de Software**. O objetivo principal é criar uma solução que colete, armazene e analise informações pessoais e comportamentais de fãs de esports, permitindo que clubes como a **FURIA** compreendam melhor seus seguidores e ofereçam experiências personalizadas.

---

## 📌 Objetivo

> Desenvolver um app ou solução (ex: Jupyter Notebook) que colete o máximo de informações sobre você mesmo como um fã de esports.

A estratégia **Know Your Fan** permite que organizações esportivas identifiquem padrões de comportamento, preferências de consumo e interação dos fãs, gerando insights valiosos.

---

## 🚀 Funcionalidades

✅ Cadastro de usuário com dados pessoais e endereço  
✅ Upload e validação de documentos com suporte a OCR via Tesseract  
✅ Simulação de leitura de redes sociais com foco em perfis ligados à FURIA  
✅ Compartilhamento de links de perfis e validação automatizada via IA  
✅ Banco de dados relacional PostgreSQL para armazenar os dados  
✅ Visualização de análises com gráficos interativos via Seaborn e Matplotlib  
✅ Interface em Jupyter Notebook (interativa e didática)  
✅ Deploy local com Docker e persistência de dados  

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11
- Jupyter Notebook
- Docker & Docker Compose
- PostgreSQL 14
- Pandas, Seaborn, Matplotlib
- Tesseract OCR
- Simulação de AI para validação de identidade e redes sociais

---

## 📁 Estrutura do Projeto

```bash
.
├── dados
│   ├── usuarios.csv
│   ├── enderecos.csv
│   └── redes_sociais.csv
├── notebooks
│   ├── main.ipynb                 # Notebook principal com toda a jornada
│   ├── database_setup.py          # Criação do banco e tabelas
│   ├── data_importer.py           # Importação de dados de exemplo
│   ├── db_utils.py                # Utilitários de conexão ao banco
│   ├── id_extractor.py            # OCR para documentos
│   ├── identity_validator.py      # Validação via AI (simulada)
│   ├── interactive_form.py        # Formulário com widgets
│   └── social_media_updater.py   # Simulação de leitura de redes sociais
├── img
│   └── diagrama_banco_de_dados.png  # ← [INSERIR AQUI DIAGRAMA DO BANCO]
├── docker-compose.yml
├── requirements.txt
└── README.md


## 🚀 Como Rodar com Docker

### ✅ Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### ⚙️ Passos

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/know-your-fan-furia.git
cd know-your-fan-furia

# 2. Suba os containers
docker-compose up --build

## 🚀 Acesso ao Jupyter Notebook

O Jupyter Notebook estará disponível em:  
🔗 **http://localhost:8888**  
🔐 **Token de acesso:** `secret`

---

## 🧩 Visão Geral das Funcionalidades

### 📝 Cadastro de Fã

Formulário interativo para coleta de:

- Nome, CPF, Gênero, Email, Data de Nascimento  
- Jogos e times favoritos  
- Frequência de consumo de conteúdo e eventos de esports  
- Produtos desejados e compras recentes  

📷 *[INSERIR IMAGEM DO FORMULÁRIO AQUI]*

---

### 📄 Validação de Identidade com AI

- Upload de documento e extração de informações via OCR com Tesseract  
- Simulação de validação automática com base no CPF e nome extraído

---

### 📱 Integração com Redes Sociais

Simulação de vinculação com redes sociais como Instagram e Twitter.

**Exemplo de retorno:**


```bash
Processando: Instagram - @joaosilva

📊 Páginas seguidas: @furia, @csgo, @lolesports

💡 Interações recentes:
Curtida em foto - 18h atrás
Comentário: "😍" - 17h atrás
Story visualizado
```

---

## 📊 Análises Geradas

- 🌍 **Distribuição Geográfica dos Fãs**  
  Gráfico de barras com os estados com maior concentração de fãs.

- 🎯 **Produtos Mais Desejados**  
  Top 10 produtos mais citados como desejados.

- 💸 **Histórico de Compras**  
  Proporção de fãs que já realizaram compras relacionadas a esports.

- 🎮 **Jogos Favoritos**  
  Ranking dos 10 jogos mais citados pelos fãs.

---

## 🧱 Banco de Dados

O projeto utiliza **PostgreSQL** com as seguintes tabelas:

### 🔢 Tabelas

- **Usuarios**  
  Contém dados pessoais, jogos, times, eventos e interesses.

- **Redes_Sociais**  
  Associa perfis de redes sociais ao usuário e armazena interações.

- **Enderecos**  
  Relaciona localizações e endereços aos usuários cadastrados.

📷 Diagrama do banco de dados:  
![Diagrama do Banco de Dados](img/imagem.png)

---

## 📫 Contato

Feito com dedicação por **[Seu Nome]**  
📧 [rafael.brambilla3@gmail.com]  
🔗 [https://www.linkedin.com/in/rafaelviniciusbrambillaalves/](https://www.linkedin.com/in/rafaelviniciusbrambillaalves/

---

## 🧠 Observações Finais

Este projeto é **educacional** e foi construído com **dados fictícios**, utilizando simulações de AI e redes sociais. Nenhuma informação real de terceiros foi utilizada.

---