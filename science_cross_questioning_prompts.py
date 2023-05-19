prompt_get_answer = """
provide the answer such that a student of class {class_no} can understand the answer
question: {input_question}
answer:
"""
prompt_get_entities = """
sentence: {question}
primary_concepts:
""" 

prompt_get_questions = """
Generate 2 concise questions. For each question connect any one random entity from the list {list_secondary_concepts} to the {list_primary_concepts}.  
"""

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

create MCQ for the strings in the list. MCQ and the explanation should be suitable for a student of class {class_no}  
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















# prompt_get_answer = """
# question: {input_question}
# answer:
# """
# prompt_get_entities = """ 
# identify the Entities from the sentence
# sentence: {text}
# entities:    
# """

# prompt_get_questions = """
# Generate 2 concise questions connecting any one random entity from the list {list_secondary_concepts} to the {list_primary_concepts} for each question    
# """