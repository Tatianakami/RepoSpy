from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    contexto = navegador.new_context()
    pagina = contexto.new_page()

    # Acessa a aba de repositórios
    pagina.goto("https://github.com/Tatianakami?tab=repositories")
    pagina.wait_for_selector('h3.wb-break-all a')

    # Captura os nomes e links dos repositórios
    repositorios = pagina.locator('h3.wb-break-all a').all()
    lista_links = []

    print("\n📦 Repositórios públicos encontrados:")
    for i, repo in enumerate(repositorios):
        nome = repo.text_content().strip()
        link = repo.get_attribute("href")
        lista_links.append(link)
        print(f"{i + 1}. {nome} → https://github.com{link}")

    # Escolha do repositório
    escolha = input("\nDigite o número do repositório que deseja abrir: ")
    try:
        indice = int(escolha) - 1
        if 0 <= indice < len(lista_links):
            link_escolhido = f"https://github.com{lista_links[indice]}"
            nova_pagina = contexto.new_page()
            nova_pagina.goto(link_escolhido)
            nova_pagina.wait_for_timeout(2000)

            # Tenta extrair a descrição
            descricao_elemento = nova_pagina.locator("div.BorderGrid-cell p")
            descricao = descricao_elemento.first.text_content().strip() if descricao_elemento.count() > 0 else "Descrição não encontrada."

            # Tenta extrair a linguagem principal
            linguagem_elemento = nova_pagina.locator("li.d-inline span[itemprop='programmingLanguage']")
            linguagem = linguagem_elemento.first.text_content().strip() if linguagem_elemento.count() > 0 else "Linguagem não identificada."

            print(f"\n🔍 Detalhes do repositório selecionado:")
            print(f"📄 Descrição: {descricao}")
            print(f"💻 Linguagem principal: {linguagem}")
        else:
            print("Número inválido.")
    except Exception as e:
        print("Erro ao abrir o repositório:", e)

    # Fecha o navegador corretamente
    input("\nPressione Enter para fechar o navegador...")
    navegador.close()

