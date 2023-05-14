import openai
import os
from science_cross_questioning_functions import get_primary_answer, get_secondary_answer,create_prompts, mcq_cross_questioning

openai.api_key = ''

input_query = 'what is a rainbow?'
student_class = '10'
primary_answer, primary, secondary = get_primary_answer(input_query, student_class)
secondary_answer = get_secondary_answer(input_query, student_class)
prompts_output = create_prompts(primary, secondary)
mcq_science = mcq_cross_questioning(prompts_output, student_class)

print(input_query)
print(primary_answer)
print(primary,secondary)
print(secondary_answer)
print(prompts_output)
print(mcq_science)
