from playwright.sync_api import sync_playwright

# Função de automação
def automate_google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navegar para o site do Google
        page.goto('https://www.google.com')

        # Preencher o campo de pesquisa com "Python" e pressionar Enter
        page.fill('input[name="q"]', 'Python')
        page.press('input[name="q"]', 'Enter')

        # Aguardar a página de resultados carregar
        page.wait_for_selector('.g')

        # Capturar títulos dos resultados da pesquisa
        search_results = page.query_selector_all('.g h3')

        # Imprimir os títulos dos resultados
        for result in search_results:
            print(result.text_content())

        # Fechar o navegador
        browser.close()

# Chamar a função de automação
automate_google_search()
