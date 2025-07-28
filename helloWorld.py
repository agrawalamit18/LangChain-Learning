import os
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain

promoptTemplate = PromptTemplate(
    input_variables=["countryname"],
    template="Capital of country {countryname}",
    output_variables=["capital_name"]  # Specify the output variable for the next chain
)

promoptTemplate1 = PromptTemplate(
    input_variables=["capital_name"],
    template="Population of city {capital_name}",
    output_variables=["population"]  # Specify the output variable for the next chain
)

    # Initialize the Ollama LLM
llm = OllamaLLM(model="llama3.2", temperature=0.7)

chain = promoptTemplate |llm

chain1 = promoptTemplate1 |llm

# Invoke the LLM with a prompt
#simpleSequentialChain = SimpleSequentialChain(chains=[chain, chain1])
#reponse = SimpleSequentialChain.run("India")

response = chain.invoke({"India"})

print(response)