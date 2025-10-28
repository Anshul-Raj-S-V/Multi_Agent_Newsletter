from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os
load_dotenv()
# Setup the tool for internet searching capabilities
google_search_tool = SerperDevTool(api_key=os.getenv("SERPER_API_KEY"))

