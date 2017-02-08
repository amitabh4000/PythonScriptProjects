import os
import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
for randQuiz in range(1,36):
    dirName = "Quiz" + str(randQuiz)
    absPath = os.path.abspath('.')
    dirPath = os.path.join(absPath , dirName)
    os.makedirs(dirPath)
    os.chdir(dirPath)
    quizFile = open("Quiz.txt" , 'a')
    answerFile = open ("Answers.txt" , 'a')
    quizFile.write(" GEOGRAPHY QUIZ \n");
    quizFile.write("********Please select correct Capital for the states ******* \n")
    states = list(capitals.keys())
    random.shuffle(states)
    for questionNum in range(50):
        quizFile.write(str(questionNum + 1) +") " +
                       "What is the capital of: " +
                       states[questionNum] +"? \n")
        answer = capitals[states[questionNum]]
        answerFile.write(str(questionNum + 1) +") " + answer + "\n")
        answers = []
        answers.append(answer)
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(answer)]
        wrongAnswers = random.sample(wrongAnswers , 3)
        answers.extend(wrongAnswers)
        index = 0
        for option in answers:
            quizFile.write("\t" + chr(ord('A') + index) +") "+option + "\n")
            index += 1
    quizFile.close()
    answerFile.close()
    os.chdir('../')
