from crewai_tools import ScrapeWebsiteTool, SerperDevTool

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class SimilarFrameworkFinderTemplateCrew:
    """SimilarFrameworkFinderTemplate crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def platform_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["platform_analyst"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def market_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["market_researcher"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def similarity_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config["similarity_evaluator"],
            tools=[],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def consultation_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config["consultation_strategist"],
            tools=[],
            allow_delegation=False,
            verbose=True,
        )

    @task
    def analyze_target_platform_task(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_target_platform_task"],
            agent=self.platform_analyst(),
        )

    @task
    def find_potential_similar_platforms_task(self) -> Task:
        return Task(
            config=self.tasks_config["find_potential_similar_platforms_task"],
            agent=self.market_researcher(),
        )

    @task
    def evaluate_similarity_task(self) -> Task:
        return Task(
            config=self.tasks_config["evaluate_similarity_task"],
            agent=self.similarity_evaluator(),
        )

    @task
    def develop_approach_recommendations_task(self) -> Task:
        return Task(
            config=self.tasks_config["develop_consultation_recommendations_task"],
            agent=self.consultation_strategist(),
            output_file="consultation_recommendations.md",
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
