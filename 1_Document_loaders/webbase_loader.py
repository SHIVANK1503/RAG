# WebBaseLoader is a document loader in langchain and extract text conteny from web pages(URLs). It uses BeautifulSoup under the hood to parse HTML and extract visible text.
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import  ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://strapi.io/blog/what-is-a-static-website"
loader = WebBaseLoader(url)
docs = loader.load()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview", google_api_key = os.getenv('GOOGLE_API_KEY'))

parser = StrOutputParser()

prompt = PromptTemplate(
    template= "Answer the question \n {question} from the following text \n {text}",
    input_variables=["question", "text"]
)

chain = prompt | model | parser
result = chain.invoke({"question":"what do you mean by static websites", "text":docs[0].page_content})

print(result)

'''
output: 
Based on the text provided, a **static website** is defined as a website that serves pre-built, fixed HTML files directly to the user's browser exactly as they are stored, without any server-side processing or database queries at the time of the request.

Key characteristics and implications of static websites mentioned in the text include:

*   **Content Consistency:** Every visitor sees the exact same content regardless of their location or device.
*   **Pre-rendered Pages:** The files are built before deployment rather than being generated on the fly when a user visits the page.
*   **Performance and Security:** Because there is no server-side logic or database access during a request, static sites are highly secure (reducing attack surfaces) and offer fast load times.
*   **Updates:** Content generally stays the same for everyone and only changes when a developer updates the source code or triggers a rebuild/redeployment.
*   **Core Technologies:** They rely on the foundational trio of web development: **HTML** (structure), **CSS** (styling), and **JavaScript** (client-side interactivity).
*   **Ideal Use Cases:** They are best suited for projects with stable, non-real-time content, such as personal blogs, company informational pages, documentation sites, portfolios, and landing pages.

The text also notes that while static websites are traditionally simple, they can be made more dynamic by integrating modern tools like **Static Site Generators (SSGs)**, **Headless CMS platforms (like Strapi)**, and the **Jamstack architecture**, which allow for dynamic features without sacrificing the performance and security benefits of a static build.
'''

''' 
Advantage -> For blogs, news articles or public websites where the contant is text-based and static
Disadvantage -> Doesn't handle JavaScript-heavy pages well (use SeleniumURLLoaderfor that).
Loads only static content (what's in the HTML, not what loads after the page renders).
'''