from langchain.agents import initialize_agent
from langchain.llms import OpenAI
import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from core.commands import (computer_applescript_action,
    chrome_open_url,
    chrome_get_the_links_on_the_page,
    chrome_read_the_page,
    chrome_click_on_link)

llm = OpenAI(temperature=0, openai_api_key="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", max_tokens=6000) # type: ignore
tools = [
    computer_applescript_action,
    chrome_open_url,
    chrome_get_the_links_on_the_page,
    chrome_read_the_page,
    chrome_click_on_link,
]

agent = initialize_agent(tools, llm, initialize_agent="zero-shot-react-description", verbose=True)