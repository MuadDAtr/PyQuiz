from json import load

with open('quiz.json') as quest_file:
    questions = load(quest_file)
    #print(questions)

    for question in questions:
        print(question['question'])
        print("")
        print('~~~' *20)