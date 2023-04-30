import random
import openai
from science_cross_questioning_prompts import prompt_get_answer, prompt_get_entities, prompt_get_questions
from config import MODEL

def get_primary_answer(question):
  primary_prompt = prompt_get_answer.format(input_question = question)  
  primary_answer = openai.ChatCompletion.create(model = MODEL,temperature = 0,
      messages= [{'role': 'system', 'content': 'You are a helpful AI science tutor who provides answer for given question' },
      {'role': 'user', 'content': primary_prompt}])
  model_answer = primary_answer['choices'][0]['message']['content']
  entities_prompt = prompt_get_entities.format(question = input, answer = model_answer)
  primary_answer = openai.ChatCompletion.create(model = "gpt-3.5-turbo",temperature = 0,
      messages= [{'role': 'system', 'content': 'You are a helpful AI science Named Entity extractor'},
      {'role': 'user', 'content': entities_prompt}])
  string = primary_answer['choices'][0]['message']['content']
  # Extract primary concepts
  string = string.replace("Primary Concepts","Primary concepts")
  string = string.replace("Secondary Concepts", "Secondary concepts")

  try:
    primary_concepts = string.split("Secondary concepts")[0].replace("Primary concepts:",'').split('\n')
    primary_concepts = [x for x in primary_concepts if x != '']
    primary_concepts = [s[2:] for s in primary_concepts]
    secondary_concepts = (string.split("Secondary concepts:")[1]).split('\n')
    secondary_concepts = [x for x in secondary_concepts if x != '']
    secondary_concepts = [s[2:] for s in secondary_concepts]
    return model_answer, primary_concepts, secondary_concepts
  except:
    primary_concepts = string.split("Secondary Concepts")[0].replace("Primary Concepts:",'').split('\n')
    primary_concepts = [x for x in primary_concepts if x != '']
    primary_concepts = [s[2:] for s in primary_concepts]
    secondary_concepts = (string.split("Secondary Concepts:")[1]).split('\n')
    secondary_concepts = [x for x in secondary_concepts if x != '']
    secondary_concepts = [s[2:] for s in secondary_concepts]
    return model_answer, primary_concepts, secondary_concepts


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

  
