from crewai_tools import ScrapeWebsiteTool, SerperDevTool

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class SimilarFrameworkFinderTemplateCrew:
    """SimilarFrameworkFinderTemplate crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["analysis_agent"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def recommendation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["recommendation_agent"],
            tools=[],
            allow_delegation=False,
            verbose=True,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
            agent=self.researcher(),
        )

    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["analysis_task"],
            agent=self.analysis_agent(),
        )

    @task
    def recommendation_task(self) -> Task:
        return Task(
            config=self.tasks_config["recommendation_task"],
            agent=self.recommendation_agent(),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SimilarCompanyFinderTemplate crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
