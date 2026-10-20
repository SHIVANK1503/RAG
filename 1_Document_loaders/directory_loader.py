# DirectoryLoader is a document loader that lets you load multiple documents from a directory (folder) of files.

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="books", # path from where multiple files need to be loaded
    glob='*pdf', # select all PDF files
    loader_cls= PyPDFLoader # name of loader used
)

# if we notice it takes to much time to run the code as it loads the all pdf file into RAM so that we can do any operation.

# but the solution is lazy_load lazy_loading gives the generator of documents which load one documnt at once and then removed from the memory.

# docs = loader.load() # load everything in once and then gives the o/p
docs = loader.lazy_load() # laxy_load load 1 document at once. it is like on demand.

# print((docs[0].page_content))

for document in docs:
    print(document.metadata)

