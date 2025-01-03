import os
import base64
from dotenv import load_dotenv
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents import initialize_agent, Tool, AgentType

load_dotenv()

_llm_instance = None

def get_llm_instance():
    global _llm_instance
    if _llm_instance == None:
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        _llm_instance = OpenAI(api_key = openai_api_key)
    return _llm_instance

def desc_image_chain(llm):
    image_desc_prompt = PromptTemplate(
        input_variables=["image_cat", "image_url", "response_type"],
        template="You are an expert {image_cat} explorer. The user has provided you with an image at this url: {image_url}. You need to provide a {response_type} response:\n\n{image_url}"
    )
    return LLMChain(llm=llm, prompt=image_desc_prompt)

def chart_analysis_chain(llm):
    chart_analysis_prompt = PromptTemplate(
        input_variables=["chart_image_url"],
        template="""
        Analyze the image of the chart or graph here:\n\n {chart_image_url}. Your tasks are to:\n\n
        1. Identify the type of chart or graph (e.g., bar chart, line graph, pie chart etc.).\n
        2. Extract the key data points, including labels, values, and any relevant scales or units.\n
        3. Identify and describe the main trends, patterns, or significant observations presented in the chart.\n
        4. Generate a clear and concise paragraph summarizing the extracted data and insights. The summary should highlight the most important information and provide an overview that would help someone understand the chart without seeing it.\n
        5. Ensure that your summary is well-structured, accurately reflects the data, and is written in a professional tone
        """
    )
    return LLMChain(llm=llm, prompt=chart_analysis_prompt)

def damage_assess_chain(llm):
    damage_assessment_prompt = PromptTemplate(
        input_variables=["car_image_before_url", "car_image_after_url"],
        template = '''
        You are a helpful ai assistant for an insurance agent. Insurance agent has received a claim for a vehicle damage. This claim includes two images. One of the image was taken before the incident and is provided at this url: {car_image_before_url}. Another image was taken after the incident and is provided at this url: {car_image_after_url}. Analyse these images and answer below questions:\n\n
            1. Describe if there is any damage to the vehicle
            2. Should insurance agent accept or reject the claim
        '''
    )
    return LLMChain(llm=llm, prompt = damage_assessment_prompt)

def product_analyzer_chain(llm):
    product_analysis_prompt = PromptTemplate(
        input_variables=["product_image_url"],
        template='''
        You are a product analyst your job is to analyze product image provided at this url: {product_image_url}. Output the information in the exact JSON structure specified below. Ensure that you populate each field accurately based on the visible details in the page. If any information is not available or cannot be determined, use 'Unknown' for string fields and empty array [] for lists. \n\n
        Use the format shown exactly, ensuring all fields and values align with JSON schema requirements. \n\n
        Generate information for the following fields: \n\n
        1. title - The name of the product
        2. description - Description of the product
        3. category - Category of the product ("Electronics","Furniture", "Luggage","Clothing","Appliances","Toys","Books","Tools","Other")
        4. price - Price of the product in USD
        5. images - An array of images
        6. brand - Brand of the product
        7. dimensions - Dimensions of the product (height, width, length)
        8. weight - Weight of the product
        9. color - Color of the product
    '''
    )
    return LLMChain(llm=llm, prompt = product_analysis_prompt)
    
def initialize_agent_executor():
    llm = get_llm_instance()
    tools = [
        Tool(
            name="DescribeImage",
            func=lambda image_url: desc_image_chain(llm).run(image_url = image_url),
            description="You are an expert nature explorer"
        ),
        Tool(
            name="ChartAnalysis",
            func = lambda chart_image_url: chart_analysis_chain(llm).run(chart_image_url = chart_image_url),
            description = "You are an expert chart or graph analysts. When the user provides you with a chart or graph, describe the analysis"
        ),
           Tool(
            name="DamageAssessment",
            func = lambda car_image_before_url, car_image_after_url: damage_assess_chain(llm).run(car_image_before_url = car_image_before_url, car_image_after_url=car_image_after_url),
            description = "You are a helpful ai assistant for an insurance agent."
        ),
          Tool(
            name="ProductDataExtraction",
            func = lambda product_image_url: product_analyzer_chain(llm).run(product_image_url = product_image_url),
            description = "You are an expert product image analyst."
        )
    ]

    agent = initialize_agent(tools,llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, return_intermediate_steps = True)
    return agent


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")