import random
import openai
from science_cross_questioning_prompts import prompt_get_answer, prompt_get_entities, prompt_get_questions, prompt_MCQ
from config import MODEL

def get_primary_answer(question, student_class):
  primary_prompt = prompt_get_answer.format(input_question =  question, class_no = student_class)  
  primary_answer = openai.ChatCompletion.create(model = MODEL,temperature = 0,
        messages= [{'role': 'system', 'content': 'You are a helpful AI science tutor who provides answer for given question' },
        {'role': 'user', 'content': primary_prompt}])
  model_answer = primary_answer['choices'][0]['message']['content']
  #print(model_answer)
  entities_prompt = prompt_get_entities.format(question = question)
  primary_answer = openai.ChatCompletion.create(model = MODEL,temperature = 0,
        messages= [{'role': 'system', 'content': 'You are a helpful AI science Named Entity extractor who provide only the entities'},
        {'role': 'user', 'content': entities_prompt}])
  string = primary_answer['choices'][0]['message']['content']
  string = string.split('\n')
  primary_concepts = []
  for i in string:
    primary_concepts.append(i[2:])
  #print(primary_concepts)
  entities_prompt = prompt_get_entities.format(question = model_answer)
  primary_answer = openai.ChatCompletion.create(model = MODEL,temperature = 0,
        messages= [{'role': 'system', 'content': 'You are a helpful AI science Named Entity extractor who provide only the entities'},
        {'role': 'user', 'content': entities_prompt}])
  string = primary_answer['choices'][0]['message']['content']
  secondary_concepts = string.split('\n')
  #print(secondary_concepts)
  return model_answer, primary_concepts, secondary_concepts

def get_secondary_answer(input_prompt, student_class):
  primary_prompt = prompt_get_answer.format(input_question = input_prompt, class_no = student_class)  
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


def mcq_cross_questioning(read, student_class):
  mcq_prompt = prompt_MCQ.format(prompt_read = read, class_no = student_class)
  mcq_generator = openai.ChatCompletion.create(model = MODEL,temperature = 0,
        messages= [
        {'role': 'system', 'content': 'You are multiple choice Question generator, who generates 3 multilple choice questions with 4 options, answers and explanations for the strings in the given listt' },
        {'role': 'user', 'content': mcq_prompt}])
  mcq = mcq_generator['choices'][0]['message']['content']
  output_split = mcq.split('\n')
  output_strip = []
  for i in output_split:
    output_strip.append(i.strip())
  output_strip = [i for i in output_strip if i] # To remove any empty strings
  output_strip
  question = []
  answers = []
  options = []
  explanations = []

  for i, string in enumerate(output_strip):
      if 'Question' in string:
          question.append(string.split('Question ')[1][2:].strip())
      elif 'Answer' in string:
          answers.append(string.split('Answer:')[1][3:].strip())
      elif 'Explanation' in string:
        explanations.append(string.split('Explanation:')[1].strip())
      elif 'Options' in string:
          options.append([output_strip[i+1][2:].strip(), output_strip[i+2][2:].strip(), output_strip[i+3][2:].strip(), output_strip[i+4][2:].strip()])

  mcq_json_list = []
  for i in range(len(question)):
      mcq_json = {}
      mcq_json['Question'] = question[i]
      mcq_json['Answer'] =  answers[i]
      mcq_json['Options'] = options[i]
      mcq_json['Explanation'] = explanations[i]
      mcq_json_list.append(mcq_json)
  return mcq_json_list


















# def get_primary_answer(question):
#   primary_prompt = prompt_get_answer.format(input_question = question)  
#   primary_answer = openai.ChatCompletion.create(model= MODEL, temperature = 0,
#         messages= [{'role': 'system', 'content': 'You are a helpful AI science tutor who provides answer for given question' },
#         {'role': 'user', 'content': primary_prompt}])
#   model_answer = primary_answer['choices'][0]['message']['content']
#   #print(model_answer)
#   entities_prompt = prompt_get_entities.format(text = question)
#   primary_ans_entities = openai.ChatCompletion.create(model = MODEL,temperature = 0,
#         messages= [{'role': 'system', 'content': 'You are a helpful AI science Entity extractor'},
#         {'role': 'user', 'content': entities_prompt}])
#   primary = primary_ans_entities['choices'][0]['message']['content'].split('\n')
#   primary_entity = [item.strip('- ') for item in primary]
#   primary_entity = [item.replace('"', '') for item in primary_entity]
#   #primary
#   entities_prompt = prompt_get_entities.format(text = model_answer)
#   secondary_ans_entities = openai.ChatCompletion.create(model = MODEL,temperature = 0,
#         messages= [{'role': 'system', 'content': 'You are a helpful AI science Named Entity extractor'},
#         {'role': 'user', 'content': entities_prompt}])
#   secondary = secondary_ans_entities['choices'][0]['message']['content'].split('\n')
#   secondary_entity = [item[2:].strip() if item[0].isdigit() else item for item in secondary]
#   #print(secondary)
#   #print(prompt_generated_processed)
#   return model_answer, primary_entity, secondary_entity 


# def get_secondary_answer(input_query):
#   primary_prompt = prompt_get_answer.format(input_question = input_query)  
#   primary_answer = openai.ChatCompletion.create(model = MODEL,temperature = 0,
#       messages= [{'role': 'system', 'content': 'You are a helpful AI science tutor who provides answer for given question' },
#       {'role': 'user', 'content': primary_prompt}])
#   model_answer = primary_answer['choices'][0]['message']['content']
#   return model_answer

# def create_prompts(primary_concepts, secondary_concepts):
#   prompt_generated_processed = []
#   secondary_concepts_entity = random.choice(secondary_concepts)
#   question_prompt = prompt_get_questions.format(list_secondary_concepts = secondary_concepts_entity, list_primary_concepts = primary_concepts)
#   prompt_generator = openai.ChatCompletion.create(model = MODEL,temperature = 0,
#       messages= [
#       {'role': 'user', 'content': question_prompt}])
#   prompt_generated = prompt_generator['choices'][0]['message']['content'].split('\n')
#   prompt_generated = [i[2:].strip() for i in prompt_generated]
#   #print(prompt_generated)
#   return prompt_generated

  
