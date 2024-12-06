#!/usr/bin/env python
import sys

from similar_framework_finder_template.crew import SimilarFrameworkFinderTemplateCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    inputs = {
        "Product_Category": "Cereal", 
        "Target_Brands": "Honey Bunches of Oats, Kellogg's",
        "Key_Features": "Low in sugar, No artificial colors or flavors, No preservatives",
    }

    SimilarFrameworkFinderTemplateCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "Low code, no code AI Application Development"}
    try:
        SimilarFrameworkFinderTemplateCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SimilarFrameworkFinderTemplateCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "Low code, no code AI Application Development"}
    try:
        SimilarFrameworkFinderTemplateCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
