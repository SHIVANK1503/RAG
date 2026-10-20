# pyPDF loader converts PDF files and convert each page into a Document object.
# Limitations: It uses the PyPDF library under the hood — not great with scanned PDF or complex layouts.

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')
docs = loader.load() 

print(docs[0].page_content)
print(docs[0].metadata)

'''Use Case                           Recommended Loader
Simple, clean PDFs             ->      PyPDFLoader
PDFs with tables/columns       ->      PDFPlumberLoader
Scannedßmage PDFs              ->      UnstructuredPDFLoader or AmazonTextractPDFLoader
Need layout and image data     ->      PyMuPDFLoader
Want best structure extraction ->      UnstructuredPDFLoader '''


