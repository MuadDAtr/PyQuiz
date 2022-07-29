from json import load

points_counter = 0

with open('quiz.json') as quest_file:
    questions = load(quest_file)
    #print(questions)

    for question in questions:
        print(question['question'])
        print("")
        for index, answer in enumerate(question['answers'], 1):
            print(index, answer['ans'])
        print("")
        
        users_answer = int(input("What's your answer?  "))
        print("")
        print('~~~'*20)

    