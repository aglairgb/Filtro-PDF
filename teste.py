import pdfplumber

def filtrar_dados_pdf(caminho_arquivo):
    dados_filtrados = []
    with pdfplumber.open(caminho_arquivo) as pdf:
        for page in pdf.pages:
            text_content = page.extract_text()
            items = text_content.strip().split("\n")

            for j in range(len(items)-1):
                descricao = items[j]
                preco = items[j+1]

                if "269ML" in descricao:
                    dados_filtrados.append({"descricao": descricao, "preco": preco})

    return dados_filtrados

caminho_pdf = "./Oasis.pdf"
dados_filtrados = filtrar_dados_pdf(caminho_pdf)
for dado in dados_filtrados:
    print("Descrição:", dado["descricao"])
    print("Preço:", dado["preco"])
    print()
