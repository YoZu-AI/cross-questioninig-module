import openai
from new_module_prompt import MCQ_prompt
openai.api_key = ''

def get_science_concepts(input_query):
  completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0,
    messages=[
      {"role": "system", "content": 'You are an expert science AI assistant, you will list 5 concepts name necessary to answer the given query, without giving explanation of each concepts'},
      {"role": "user", "content": input_query}])
  science_concepts  = completion.choices[0].message.content.split('\n')
  science_concepts 
  science_concepts_list = []
  for sentence in science_concepts:
      if len(sentence) >= 3 and sentence[0].isdigit() and sentence[1] == '.':
          science_concepts_list.append(sentence[2:].strip())       
  return science_concepts_list

def get_science_concept_explanation(concepts_list, student_class):
  definition_prompt = 'The given list is {pre_knowledge}. Provide the precise and best possible explanation with the help of an example to each of the topics in the given list so that a student of class {class_no} can easily understand the definition and example. Follow the the format, Topic: , Definition:, Example:'
  input_definition_prompt = definition_prompt.format(pre_knowledge = str(science_concepts_list), class_no = student_class)
  completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0,
    messages=[
      {"role": "system", "content": 'You are an expert science AI tutor.'},
      {"role": "user", "content": input_definition_prompt}])
  science_concepts_explanation = completion.choices[0].message.content 
  science_concepts_explanation_split = science_concepts_explanation.split('\n')
  topic = []
  definition = []
  example = []
  for i in science_concepts_explanation_split:
    if i != '':
      if 'Topic' in i:
        topic.append(i.split('Topic:')[1].strip())
      if 'Definition' in i:
        definition.append(i.split('Definition:')[1].strip())
      if 'Example' in i:
        example.append(i.split('Example:')[1].strip())
  return topic, definition , example

def get_detailed_science_definition(previous_definition, student_class):
  prompt = 'provides the simpler and detailed explanation of the definition, {definition}. Explanation should be suitable for a student studying in class {class_no}'
  provide_definition_explanation_prompt = prompt.format(definition = previous_definition, class_no = student_class)
  completion = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  temperature = 0,
  messages=[
      {"role": "system", "content": 'You are an expert science AI tutor who provides the simpler and detailed explanation of the given input'},
      {"role": "user", "content": provide_definition_explanation_prompt}])
  return(completion.choices[0].message.content)

def get_pre_concept_mcq(science_concepts_list, student_class):
  MCQ_concept_prompt = MCQ_prompt.format(science_concept = str(science_concepts_list), class_no = student_class)
  completion = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  temperature = 0,
  messages=[
        {"role": "system", "content": 'You are an expert science AI tutor who generates the MCQ for the items in the given list'},
        {"role": "user", "content": MCQ_concept_prompt }])
  science_split = completion.choices[0].message.content.split('\n')
  science_split = [item for item in science_split if item != ' ']
  science_split
  pre_question = []
  pre_answer = []
  pre_explanation = []
  pre_options = []

  for i, string in enumerate(science_split):
    if 'Question' in string:
      pre_question.append(string.split('Question:')[1].strip())
    if 'Answer' in string:
      pre_answer.append(string.split('Answer:')[1][3:].strip())
    if 'Explanation' in string:
      pre_explanation.append(string.split('Explanation:')[1].strip())
    elif 'Options' in string:
      pre_options.append([science_split[i+1][2:].strip(), science_split[i+2][2:].strip(), science_split[i+3][2:].strip(), science_split[i+4][2:].strip()]) 

  mcq_json_pre_list = []
  for i in range(len(pre_question)):
      mcq_json = {}
      mcq_json['Question'] = pre_question[i]
      mcq_json['Answer'] =  pre_answer[i]
      mcq_json['Options'] = pre_options[i]
      mcq_json['Explanation'] = pre_explanation[i]
      mcq_json_pre_list.append(mcq_json)
  return mcq_json_pre_list

def science_solution(science_query, class_no):
  science_prompt = 'Provide a precise and concise answer to the query, {query}. Answer should be suitable for students in studying in {student_class}th class'
  prompt_input = science_prompt.format(query = science_query, student_class = class_no)
  #print(prompt_input)
  completion = openai.ChatCompletion.create(model = 'gpt-3.5-turbo',temperature = 0,
  messages=[{'role': 'system', 'content': 'You are a kind and helpful science AI tutor who provide clear and concise answer'},
        {'role': 'user', 'content': prompt_input}])
  return completion['choices'][0]['message']['content']

def get_detailed_science_solution(previous_solution, student_class):
  prompt_format = 'provide detailed explanation of the following, {solution}. explanation should be easy to understand and simpler but in great detail so that a student of class {class_no} can understand'
  prompt = prompt_format.format(solution = previous_solution, class_no = student_class)
  completion = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  temperature = 0,
  messages=[
     {"role": "system", "content": 'You are an expert science AI tutor who provides the simpler and detailed explanation of solution for the query'},
     {"role": "user", "content": prompt}])
  return completion.choices[0].message.content
  #return completion.choices[0].message.content

##########################################################################

input_query = 'what is a fruit'
student_class = '8'

science_concepts_list = get_science_concepts(input_query)
topic, definition, example = get_science_concept_explanation(science_concepts_list, student_class)
previous_definition = definition[0]
detailed_definition = get_detailed_science_definition(previous_definition, student_class)
pre_concept_mcq = get_pre_concept_mcq(science_concepts_list, student_class) 
ans = science_solution(input_query, student_class)
detailed_science_solution = get_detailed_science_solution(ans, student_class)




print(science_concepts_list)
print(topic)
print(definition)
print(example)
print(previous_definition)
print(detailed_definition)
print(pre_concept_mcq)
print(ans)
print(detailed_science_solution)