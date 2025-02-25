# src/latest_ai_development/crew.py
import logging

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, after_kickoff, agent, before_kickoff, crew, task
from crewai_tools import SerperDevTool

logging.basicConfig(level=logging.DEBUG)

# GitHub Models llm
"""
llm = LLM(
    model="openai/gpt-4o", # call model by provider/model_name
    base_url="https://models.github.ai/inference",
    temperature=0.8,
    max_tokens=150,
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1,
    stop=["END"],
    seed=42
)
How would we pass as the global llm?
"""


@CrewBase
class LatestAiDevelopmentCrew:
    """LatestAiDevelopment crew"""

    @before_kickoff
    def before_kickoff_function(self, inputs):
        print(f"Before kickoff function with inputs: {inputs}")
        return inputs  # You can return the inputs or modify them as needed

    @after_kickoff
    def after_kickoff_function(self, result):
        print(f"After kickoff function with result: {result}")
        return result  # You can return the result or modify it as needed

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(config=self.agents_config["reporting_analyst"], verbose=True)

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config["reporting_task"],
            output_file="output/report.md",  # This is the file that will be contain the final report.
        )

    @crew
    def crew(self) -> Crew:
        """Creates the LatestAiDevelopment crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
