print("Welcome to QUIZ GAME!")

score = 0
#FIRST QUESTION
question_no = 0
playing = input('Do you want to play?(yes/no) ').lower()
if playing == 'yes':
    question_no += 1
    print('\n',question_no,' what does CPU stand for? ')
    ques = input("").lower()
    if ques == 'central processing unit':
        score +=1
        print('THATS RIGHT!')
        
    else:
        print('WRONG ANSWER!')
        print('CORRECT Answer is --> central processing unit')

#SECOND QUESTION
    question_no += 1
    print('\n',question_no,' what does GPU stand for? ')
    ques = input("").lower()
    
    if ques == 'graphical processing unit':
        score +=1
        print('THATS RIGHT!')
        
    else:
        print('WRONG ANSWER!')
        print('CORRECT Answer is --> graphics processing unit')

#THIRD QUESTION
    question_no += 1
    print('\n',question_no,' what does RAM stand for? ')
    ques = input("").lower()
    
    if ques == 'random access memory':
        score +=1
        print('THATS RIGHT!')
        
    else:
        print('WRONG ANSWER!')
        print('CORRECT Answer is --> random access memory')

#FOURTH QUESTION
    question_no += 1
    print('\n',question_no,' what does PSU stand for? ')
    ques = input("").lower()
    
    if ques == 'power supply unit':
        print('THATS RIGHT!')
        score+=1
        
    else:
        print('WRONG ANSWER!')
        print('CORRECT Answer is --> power supply unit')


#FIFTH QUESTION
    question_no += 1
    print('\n',question_no,' what does ROM stand for? ')
    ques = input("").lower()
    
    if ques == 'read only memory':
        print('THATS RIGHT!')
        score+=1
        
        
    else:
        print('WRONG ANSWER!')
        print('CORRECT Answer is --> read only memory')




else:
    print('thankyou you are out of a game.')
    quit()

print('\nnumber of question is ',question_no)
print('your score is ',score)
try:
    percentage = (score *100)/question_no
except ZeroDivisionError:
    print('0% quetions are correct')

print(percentage,' of the questions are correct.')