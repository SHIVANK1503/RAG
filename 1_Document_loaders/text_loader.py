# text loader gives the output in Document object format -> [Document(metadata = {}, page_content = " ")
# so to access the page content part we use -> docs = TextLoader.load => docs[0].page_content

from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

loader = TextLoader('cricket.txt', encoding='utf-8')

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview", google_api_key = os.getenv('GOOGLE_API_KEY'))

prompt = PromptTemplate(
    template="Write a summary for the following poem - \n {poem}",
    input_variables= ["poem"]
)

parser =  StrOutputParser()

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({"poem":docs[0].page_content})

print(result)

# output
'''
The summary can be broken down into three key themes:

*   **The Drama of the Game:** The poem meticulously tracks the ebb and flow of a cricket match—from the tension of the coin toss and the technical duel between batter and bowler to the heart-stopping climax of a final-ball finish. It paints a vivid picture of the sensory experience: the crack of the willow, the roar of the crowd, the strategic "chessboard" mind of the captain, and the high-stakes pressure of the scoreboard.
*   **A Bridge Across Humanity:** Beyond the professional arenas and iconic stadiums, the poem emphasizes how cricket transcends borders, ages, and backgrounds. It connects the "barefoot boys" playing in dusty lanes to the legends of the game (like Tendulkar, Lara, and Dhoni). It highlights how the sport unites families, nations, and cultures, acting as a shared legacy passed from one generation to the next.
*   **The Soul of the Sport:** Ultimately, the poem suggests that cricket is a repository for human emotion. It is a story of grit, honor, and grace that persists through every format—from the quick pace of T20 to the endurance of Test matches. The poem concludes that as long as there is a "willow and a ball," the game will continue to foster dreams and bring people together, existing as a timeless tradition that turns moments of play into lifelong memories.
'''



