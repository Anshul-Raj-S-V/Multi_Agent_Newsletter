import gradio as gr
import time
import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import researcher, writer, proof_reader
from task import research_task, write_task, proof_read_task

# Load environment variables
load_dotenv()

# Function to run the CrewAI pipeline
def generate_news(topic):
    try:
        crew = Crew(
            agents=[researcher, writer, proof_reader],
            tasks=[research_task, write_task, proof_read_task],
            process=Process.sequential,
        )

        # Slight pause for rate limits or stability
        time.sleep(2)

        # Run the pipeline
        result = crew.kickoff(inputs={"topic": topic})

        # Return only the final refined output
        return f"### 📰 Final Report on **{topic}**\n\n{result}"
    except Exception as e:
        return f"❌ **Error:** {str(e)}"

# Gradio Interface
iface = gr.Interface(
    fn=generate_news,
    inputs=gr.Textbox(label="Enter a Topic 🧠", placeholder="e.g. Artificial Intelligence in Finance"),
    outputs=gr.Markdown(label="📰 Final Output"),
    title="🧠 Multi-Agent News Generator",
    description="Enter any topic and let the Researcher, Writer, and Proofreader agents create a refined report.",
    allow_flagging="never",
    live=False,
)

# Launch the app
if __name__ == "__main__":
    iface.launch()
