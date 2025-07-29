# 🔎 GitHub Repositories Scraper with Playwright

Este projeto utiliza **Playwright (Python)** para acessar automaticamente a aba de repositórios públicos de um perfil no GitHub, listar os repositórios encontrados e permitir ao usuário explorar detalhes como descrição e linguagem principal do repositório selecionado.

![GitHub Scraper Demo](https://media.giphy.com/media/l0HUpt2s9Pclgt9Vm/giphy.gif)

## 📌 Funcionalidades

- Acesso automatizado à aba de repositórios públicos de um perfil no GitHub
- Captura dinâmica de nomes e links de repositórios
- Permite ao usuário selecionar um repositório para visualização detalhada
- Extração da descrição e linguagem principal do projeto
- Interface simples no terminal
- Execução com navegador visível (modo não headless)

## 🚀 Tecnologias Utilizadas

- [Playwright para Python](https://playwright.dev/python/)
- Python 3.7+

## 🛠️ Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Crie e ative um ambiente virtual (opcional, mas recomendado):

bash
Copiar
Editar
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
Instale as dependências:

bash
Copiar
Editar
pip install playwright
playwright install
▶️ Como Executar
bash
Copiar
Editar
python nome_do_arquivo.py
Após isso, será exibida no terminal a lista de repositórios públicos de um perfil GitHub (atualmente configurado para TatianaKami). Basta inserir o número de um repositório para visualizar mais detalhes.

💡 Exemplo de Uso
bash
Copiar
Editar
📦 Repositórios públicos encontrados:
1. projeto-exemplo → https://github.com/Tatianakami/projeto-exemplo
2. bot-py → https://github.com/Tatianakami/bot-py
...

Digite o número do repositório que deseja abrir: 2

🔍 Detalhes do repositório selecionado:
📄 Descrição: Um bot automatizado usando Python e APIs.
💻 Linguagem principal: Python
📂 Personalização
Para mudar o perfil GitHub de destino, altere a URL na linha:

python
Copiar
Editar
pagina.goto("https://github.com/Tatianakami?tab=repositories")
Substitua TatianaKami pelo nome de usuário desejado.

📌 Requisitos
Python 3.7 ou superior

Navegadores suportados instalados pelo Playwright

🧹 Finalização
Ao final do processo, pressione Enter para fechar o navegador de forma segura.

📄 Licença
Distribuído sob a licença MIT. Veja LICENSE para mais informações.

🙋‍♀️ Autor
Feito com ❤️ por Tatiana  Kami