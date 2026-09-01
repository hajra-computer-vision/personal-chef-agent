
from dotenv import load_dotenv

load_dotenv()

from langchain_ollama import ChatOllama

model = ChatOllama(model = "gemma4:31b-cloud", temperature = 0)

from langchain.tools import tool
from typing import Dict, Any
from tavily import TavilyClient

tavily_client = TavilyClient()

@tool
def web_search(query: str) -> Dict[str, Any]:

    """Search the web for information"""

    return tavily_client.search(query)

@tool
def calorie_calc(food:str) -> str:

    """Look for amount of calories in each food ingredient"""

    calories = {
    # Fruits
    "apple": 95,              # 1 medium
    "banana": 105,            # 1 medium
    "orange": 62,             # 1 medium
    "mango": 150,             # 1 medium
    "pear": 101,              # 1 medium
    "peach": 59,              # 1 medium
    "grapes": 104,            # 1 cup
    "strawberries": 49,       # 1 cup
    "watermelon": 46,         # 1 cup
    "pineapple": 82,          # 1 cup

    # Vegetables
    "potato": 161,            # 1 medium
    "sweet potato": 112,      # 1 medium
    "carrot": 25,             # 1 medium
    "broccoli": 55,           # 1 cup cooked
    "spinach": 41,            # 1 cup cooked
    "tomato": 22,             # 1 medium
    "cucumber": 16,            # 1/2 cucumber
    "corn": 143,              # 1 medium ear
    "peas": 134,              # 1 cup cooked

    # Protein / meat
    "egg": 78,                # 1 large
    "chicken breast": 165,    # 100 g cooked
    "chicken thigh": 209,     # 100 g cooked
    "beef": 250,              # 100 g cooked
    "mutton": 250,            # 100 g cooked
    "lamb": 250,              # 100 g cooked
    "fish": 206,              # 100 g cooked
    "salmon": 206,            # 100 g cooked
    "tuna": 132,              # 100 g
    "shrimp": 99,             # 100 g cooked

    # Grains / bread
    "white rice": 205,        # 1 cup cooked
    "brown rice": 218,        # 1 cup cooked
    "rice": 206,              # 1 cup cooked
    "bread": 80,              # 1 slice
    "whole wheat bread": 82,  # 1 slice
    "roti": 120,              # 1 medium
    "chapati": 120,           # 1 medium
    "naan": 260,              # 1 medium
    "oatmeal": 158,           # 1 cup cooked
    "pasta": 221,             # 1 cup cooked

    # Dairy
    "milk": 103,              # 1 cup
    "whole milk": 149,        # 1 cup
    "yogurt": 150,             # 1 cup
    "cheese": 113,             # ~28 g
    "butter": 102,             # 1 tbsp

    # Fast food / prepared foods
    "pizza": 285,              # 1 slice
    "burger": 354,             # 1 burger
    "french fries": 365,       # 1 medium serving
    "hot dog": 151,            # 1
    "sandwich": 300,           # 1 average
    "fried chicken": 320,      # 1 piece
    "chicken nuggets": 280,    # ~6 pieces

    # Snacks / nuts
    "almonds": 164,            # 1 oz
    "peanuts": 166,            # 1 oz
    "walnuts": 185,            # 1 oz
    "cashews": 157,            # 1 oz
    "popcorn": 93,             # 3 cups air-popped
    "potato chips": 152,       # ~1 oz

    # Desserts / sweets
    "chocolate": 170,          # ~1 oz
    "ice cream": 207,          # 1/2 cup
    "cake": 350,               # 1 slice
    "cookie": 140,             # 1 large
    "donut": 250,              # 1
}

    food = food.lower().strip()

    if food in calories:
        return f"{food} contains approximately {calories[food]} calories."

    return f"Sorry, I don't have calorie information for {food}."


system_prompt = """

You are a personal chef of a heart patient. The user will give you a list of ingredients they have left over in their house,

and an image of open fridge. Look for the additional ingredients in the fridge. List down those ingredients.

Look for amount of calories in each ingredient using calorie calc tool.

Using the web search tool, search the web for recipes that can be made with the ingredients they have.

Return recipe suggestions and eventually the recipe instructions to the user, if requested.

"""
from langchain.agents import create_agent

agent = create_agent(
    model=model,
    tools=[web_search, calorie_calc],
    system_prompt=system_prompt
)
