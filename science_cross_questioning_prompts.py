prompt_get_answer = """
question: {input_question}
answer:
"""
prompt_get_entities = """ 
identify the Entities from the sentence
sentence: {text}
entities:    
"""

prompt_get_questions = """
Generate 2 concise questions connecting any one random entity from the list {list_secondary_concepts} to the {list_primary_concepts} for each question    
"""