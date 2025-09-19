import os
from typing import Optional

import yaml
from crewai import Agent, Crew, Task
from crewai_tools import MCPServerAdapter, SerpApiGoogleShoppingTool
from pydantic import BaseModel, Field

from agentics.core.llm_connections import get_llm_provider
from mcp import StdioServerParameters  # For Stdio Server


shopping_tool = SerpApiGoogleShoppingTool()

shop_agent = Agent(
    role="Shopping Researcher",
    goal="Find relevant products and summarize best options for a shopper",
    backstory="Expert in product search, price/feature comparisions, and sourcing links.",
    tools=[shopping_tool],
    reasoning=False,  ## when reasoning is true a plan is generated
    reasoning_steps=10,  ## maximum number of steps that will be executed in the plan
    memory=True,  ## Set true to provide context of conversation
    verbose=True,
    llm=get_llm_provider(
        "openai"),  ## OpenAI is recommended for reasoning tasks. Try out your own model
    )

shop_task = Task(
    description="""Search Google Shopping for {search_query} and return 
    top products (title, price, merchant, link).""",
    expected_output="""A list of top relevant products with title, price, merchant, link, and a short
    justification""",
    agent=shop_agent
    #output_pydantic=WebSearchReport,  ## This will generate output in the specified type format
    )
crew = Crew(
    agents=[shop_agent],
    tasks=[shop_task],
    verbose=True,
    )
result = crew.kickoff(
    inputs={"search_query": """fall knee-high boots""",
            "location" : "United States"}
    )

(print(yaml.dump(result.pydantic.model_dump(), sort_keys=False)) if result.pydantic
        else None
    )
