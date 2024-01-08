import fitz # imports the pymupdf library
import re

# doc1 = fitz.open(r"C:\Users\ftos\Documents\Development\Denso\PCP\Invoices1\K01 - CHONGQING DENSO LTDA\Inv\Packing List4.PDF") # open a document
# doc2 = fitz.open(r"C:\Users\ftos\Documents\Development\Denso\PCP\Invoices1\K01 - CHONGQING DENSO LTDA\Inv - Copia\Packing List4.PDF") # open a document
doc3 = fitz.open(r"C:\Users\ftos\Documents\Development\Denso\PCP\Invoices1\K02 - DENSO TAILAND CO. LTD\Inv\Packing List3.PDF") # NAO IMPORTA
doc4 = fitz.open(r"C:\Users\ftos\Documents\Development\Denso\PCP\Invoices1\K02 - DENSO TAILAND CO. LTD\Inv - Copia\OK Packing List4.PDF") # OK
doc5 = fitz.open(r"C:\Users\ftos\Documents\Development\Denso\PCP\Invoices1\K02 - DENSO TAILAND CO. LTD\Inv - Copia (2)\Rev1.PL_TG0_696385.pdf") # OK
doc6 = fitz.open(r"C:\Users\ftos\Documents\Development\Denso\PCP\Invoices1\K02 - DENSO TAILAND CO. LTD\Inv - Copia (3)\Packing List3.PDF")
#out = open("output.txt", "wb") # create a text output

text = ''

for page in doc6: # iterate the document pages
  text += page.get_text() #.encode('utf8') # get plain text encoded as UTF-8

pattern = (r'^\d{5}-\d{3}')

r = re.compile(pattern=pattern)


print(text)
print(r.match(text))

# print(r)



