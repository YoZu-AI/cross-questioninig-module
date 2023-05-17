MCQ_prompt = """
For the list {science_concept}, provides MCQ for each item in the list. MCQ should have 4 options. you should also provide the Correct Answer and the Explanation. The difficulty level of the question generated should be in increasing order. MCQ and Explanation should be suitable for a student studying in class {class_no}. You should follow the below format,
1.Botanical definition of fruit
  Question: Which of the following is the correct botanical definition of fruit?
  Options:
  A. The sweet and fleshy part of a plant that is eaten as dessert
  B. The mature ovary of a flowering plant, usually containing seeds
  C. The edible part of a plant that is used to add flavor to food
  D. The green part of a plant that is used for photosynthesis
  Answer: The mature ovary of a flowering plant, usually containing seeds
"""