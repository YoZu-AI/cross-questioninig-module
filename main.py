import openai
import os
from science_cross_questioning_functions import get_primary_answer, get_secondary_answer,create_prompts

open.api.key = os.getenv("OPENAI_API_KEY")

input_query = 'what is rainbow'
primary_answer, primary, secondary = get_primary_answer(input_query)
secondary_answer = get_secondary_answer(input_query)
prompts_output = create_prompts(primary, secondary)

print(input_query)
print(primary_answer)
print(primary,secondary)
print(secondary_answer)
print(prompts_output)