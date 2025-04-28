from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI
import os
from langserve import add_routes


load_dotenv()

##setup the api key
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"]=os.getenv("LANGCHAIN_TRACING_V2")



## setting up the prompt
prompt=ChatPromptTemplate.from_messages([
    ("system","translate the following into :{language}"),
    ("user","text:{text}")
])


## setting up the model
model=ChatGroq(model="gemma2-9b-it")


## setting up the string parser
parser=StrOutputParser()



## making the chain
chain=prompt | model | parser



## doing the fastapi work

app=FastAPI(title="Translator")

add_routes(app,
           chain,
           path="/chain"
           )


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)







