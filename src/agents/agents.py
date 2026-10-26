from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.tools.tools import web_search, scrape_url
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file  

#Model Initialization
llm_select = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 1st Agent: Search Agent
def build_search_agent():
    return create_agent(
        model=llm_select,
        tools=[web_search],
        system_prompt= ("You are a Search Agent. You Use the web_search tool to find information."),
    )

# 2nd Agent: Reader Agent
def build_reader_agent():
    return create_agent(
        model=llm_select,
        tools=[scrape_url],
        system_prompt= ("You are a Reader Agent. You Use the scrape_url tool to extract information from web pages."),
    )


#writer chain 
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | llm_select | StrOutputParser()


#critic_chain 

critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm_select | StrOutputParser()