from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# text = """
# Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

# These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
# """

# integration of loader + splitter
loader = PyPDFLoader(file_path=r"C:\Users\Shivank\Desktop\RAG\1_Document_loaders\dl-curriculum.pdf")
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size= 100,
    chunk_overlap= 0,  # the common no of character we need in two chunks
    separator=''
)

# result = splitter.split_text(text)
result = splitter.split_documents(docs) # split_documents is used to split the documents into the document object
print(result[0])

'''
['Space exploration has led to incredible scientific discoveries. From landing on the Moon to explori', 
'ng Mars, humanity continues to push the boundaries of what’s possible beyond our planet.\n\nThese miss', 
'ions have not only expanded our knowledge of the universe but have also contributed to advancements', 
'in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniq', 
'ues trace their roots back to innovations driven by space programs.']

if we notice here the text is being splitted just after the length of 100 characters and it will create a problem while genearting embeddings and semantic search
which will change the entire meaning of a word
'''