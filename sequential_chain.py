from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-6-luna")
prompt1 = PromptTemplate(
    template="Generate a highlight introduction of {topic}.",
    input_variables=['topic']
)
parser = StrOutputParser()
prompt2 = PromptTemplate(
    template="Given the text ```{text}```\n Give me a 5 points summary.",
    input_variables=['text']
)

chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke(dict(text="Unemployment in Pakistan"))

print(result)