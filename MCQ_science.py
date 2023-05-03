import openai
openai.api_key = ''


prompt_MCQ = """ 
create MCQ in given format
text : {prompt_read}
question:
options:
answer:
explanation:
question:
options:
answer:
explanation:
question:
options:
answer:
explanation:

"""

def mcq_cross_questioning(read):
  mcq_prompt = prompt_MCQ.format(prompt_read = read)
  mcq_generator = openai.ChatCompletion.create(model = "gpt-3.5-turbo",temperature = 0,
        messages= [
        {'role': 'system', 'content': 'You are multiple choice Question generator, who generates 3 multilple choice questions with 4 options, answers and explanations for given text' },
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
      if string.startswith('Question'):
          question.append(string.split('Question ')[1][2:].strip())
      elif 'Answer' in string:
          answers.append(string.split('Answer:')[1][3:].strip())
      elif 'Explanation' in string:
        explanations.append(string.split('Explanation:')[1].strip())
      elif string == 'Options:':
          options.append([output_strip[i+1][2:].strip(), output_strip[i+2][2:].strip(), output_strip[i+3][2:].strip(), output_strip[i+4][2:].strip()])
  return question,answers,options,explanations


read = 'What is the difference between snow and other forms of precipitation, such as rain or sleet?'
print(mcq_cross_questioning(read))