from PyPDF2 import PdfFileReader

def log_first_pdf_page():
  us_declaration_file = open("data/pdf/US_Declaration.pdf", "rb")
  pdf_reader = PdfFileReader(us_declaration_file)
  first_page = pdf_reader.getPage(0)
  first_page_text = first_page.extractText()
  print(first_page_text)
  us_declaration_file.close()