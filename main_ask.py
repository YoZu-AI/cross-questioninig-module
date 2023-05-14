import openai
openai.api_key = ''

def science_solution(science_query, class_no):
  science_prompt = 'Provide a precise and concise answer to the query, {query}. Answer should be suitable for students in studying in {student_class}th class'
  prompt_input = science_prompt.format(query = science_query, student_class = class_no)
  #print(prompt_input)
  completion = openai.ChatCompletion.create(model = 'gpt-3.5-turbo',temperature = 0,
  messages=[{'role': 'system', 'content': 'You are a kind and helpful science AI tutor who provide clear and concise answer'},
        {'role': 'user', 'content': prompt_input}])
  return completion['choices'][0]['message']['content']

######################################################
science_query  = 'what is photosynthesis'
class_no = '10'

print(science_solution(science_query, class_no))
