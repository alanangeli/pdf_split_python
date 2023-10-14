import PyPDF2

# Caminho para o arquivo PDF de entrada com 500 páginas
pdf_file = r'C:\Users\psace\Downloads\1a500.pdf'

# Diretório de saída para os arquivos PDF individuais
output_dir = r'C:\Users\psace\Downloads\certificados'

# Abre o arquivo PDF de entrada
with open(pdf_file, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Verifica se o arquivo PDF tem pelo menos 500 páginas
    if len(pdf_reader.pages) < 500:
        print("O arquivo PDF não possui 500 páginas.")
    else:
        for page_number in range(500):
            # Cria um novo arquivo PDF para cada página
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_number])

            # Salva o novo arquivo PDF
            pdf_filename = f"{output_dir}pagina_{page_number + 1}.pdf"
            with open(pdf_filename, 'wb') as new_pdf_file:
                pdf_writer.write(new_pdf_file)

print("Divisão concluída.")