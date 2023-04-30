import random
import openai
from science_cross_questioning_prompts import prompt_get_answer, prompt_get_entities, prompt_get_questions
from config import MODEL

def get_primary_answer(question):
  primary_prompt = prompt_get_answer.format(input_question = question)  
  primary_answer = openai.ChatCompletion.create(model= MODEL, temperature = 0,
        messages= [{'role': 'system', 'content': 'You are a helpful AI science tutor who provides answer for given question' },
        {'role': 'user', 'content': primary_prompt}])
  model_answer = primary_answer['choices'][0]['message']['content']
  #print(model_answer)
  entities_prompt = prompt_get_entities.format(text = question)
  primary_ans_entities = openai.ChatCompletion.create(model = MODEL,temperature = 0,
        messages= [{'role': 'system', 'content': 'You are a helpful AI science Entity extractor'},
        {'role': 'user', 'content': entities_prompt}])
  primary = primary_ans_entities['choices'][0]['message']['content'].split('\n')
  primary_entity = [item.strip('- ') for item in primary]
  primary_entity = [item.replace('"', '') for item in primary_entity]
  #primary
  entities_prompt = prompt_get_entities.format(text = model_answer)
  secondary_ans_entities = openai.ChatCompletion.create(model = MODEL,temperature = 0,
        messages= [{'role': 'system', 'content': 'You are a helpful AI science Named Entity extractor'},
        {'role': 'user', 'content': entities_prompt}])
  secondary = secondary_ans_entities['choices'][0]['message']['content'].split('\n')
  secondary_entity = [item[2:].strip() if item[0].isdigit() else item for item in secondary]
  #print(secondary)
  #print(prompt_generated_processed)
  return model_answer, primary_entity, secondary_entity 


def get_secondary_answer(input_query):
  primary_prompt = prompt_get_answer.format(input_question = input_query)  
  primary_answer = openai.ChatCompletion.create(model = MODEL,temperature = 0,
      messages= [{'role': 'system', 'content': 'You are a helpful AI science tutor who provides answer for given question' },
      {'role': 'user', 'content': primary_prompt}])
  model_answer = primary_answer['choices'][0]['message']['content']
  return model_answer

def create_prompts(primary_concepts, secondary_concepts):
  prompt_generated_processed = []
  secondary_concepts_entity = random.choice(secondary_concepts)
  question_prompt = prompt_get_questions.format(list_secondary_concepts = secondary_concepts_entity, list_primary_concepts = primary_concepts)
  prompt_generator = openai.ChatCompletion.create(model = MODEL,temperature = 0,
      messages= [
      {'role': 'user', 'content': question_prompt}])
  prompt_generated = prompt_generator['choices'][0]['message']['content'].split('\n')
  prompt_generated = [i[2:].strip() for i in prompt_generated]
  #print(prompt_generated)
  return prompt_generated

  
