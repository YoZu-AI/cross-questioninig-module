import openai
openai.api_key = ''


prompt_MCQ = """ 
create MCQ for the strings in the list
List : ['What is the difference between snow and other forms of precipitation, such as rain or sleet?','How do ice crystals form in the atmosphere to create snowflakes?']
Question 1: What causes snow to differ from other forms of precipitation, such as rain or sleet?
options:
A) Snow is formed from frozen water droplets in the atmosphere
B) Snow is formed from frozen raindrops
C) Snow is formed from frozen sleet
D) Snow is formed from frozen hailstones  
Answer:  A) Snow is formed from frozen water droplets in the atmosphere
Explanation: Snow is formed when water droplets in the atmosphere freeze into ice crystals. These ice crystals then stick together to form snowflakes. Rain is formed when water droplets in the atmosphere combine and become too heavy to remain suspended. Sleet is formed when raindrops freeze into ice pellets before reaching the ground.
Question 2: What is the process by which ice crystals form in the atmosphere to create snowflakes?
Options:
A) Ice crystals form when water droplets in the atmosphere freeze
B) Ice crystals form when water droplets in the atmosphere evaporate
C) Ice crystals form when water droplets in the atmosphere condense
D) Ice crystals form when water droplets in the atmosphere sublimate
Answer: C) Ice crystals form when water droplets in the atmosphere condense
Explanation: Ice crystals form when water droplets in the atmosphere condense onto particles, such as dust or pollen. As more water vapor condenses onto the ice crystal, it grows in size and becomes a snowflake. This process is known as the Bergeron-Findeisen process.
Question 3: What is the most common way that snowflakes form their unique shapes?
Options:
A) The temperature and humidity of the atmosphere
B) The altitude at which the snowflake forms
C) The size of the ice crystal that forms the snowflake
D) The wind speed and direction in the atmosphere
Answer: A) The temperature and humidity of the atmosphere
Explanation: The shape of a snowflake is determined by the temperature and humidity of the atmosphere in which it forms. The temperature and humidity affect the growth rate of the snowflake and the way in which the ice crystals stick together. This results in the unique and intricate shapes of snowflakes.


List: {prompt_read}
Question 1:
Options:
Answer:
Explanation:
Question 2:
Options:
Answer:
Explanation:
Question 3:
Options:
Answer:
Explanation:
"""

def mcq_cross_questioning(read):
  mcq_prompt = prompt_MCQ.format(prompt_read = read)
  mcq_generator = openai.ChatCompletion.create(model = "gpt-3.5-turbo",temperature = 0,
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
  return question,answers,options,explanations

read = ['what is a rainbow?', 'what is light?']
print(mcq_cross_questioning(read))