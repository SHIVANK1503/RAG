# It is used to load .csv file
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Social_Network_Ads.csv')

docs = loader.load()

# print(len(docs))

# It generates a seperate document object for every single row

print(docs)

# there is a example of a row that turned into a 
# Document(metadata={'source': 'Social_Network_Ads.csv', 'row': 0}, page_content='User ID: 15624510\nGender: Male\nAge: 19\nEstimatedSalary: 19000\nPurchased: 0')

# we can also create your custom DocumentLoaders