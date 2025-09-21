#Credit: Christian P. Mariano
title='Welcome to Test your Knowledge'
greetings='bye'
print('------------------------------------------------------------')
print(title.center(60," "))
print('------------------------------------------------------------')
print('this game we will test your knowlegde in philippines history')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=10
 
if answer.lower()=='yes':
  
    answer=input('Question 1: he  was considered as brain of katipunan?: ')
    if answer.lower()=='emilio jacinto':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
      
    answer=input('Question 2: he was the founder of la liga filipino?: ')
    if answer.lower()=='jose rizal':
   
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 3: was killed at near Mount Nagpatong (or Mount Buntis) in San Diego?: ')
    if answer.lower()=='andres bonifascio':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
        
        answer=input('Question 4: he was mastermind of the revolution ')
    if answer.lower()=='apolinario mabini':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
      
    answer=input('Question 5: what is original title of the national anthem in philippines?: ')
    if answer.lower()=='marcha filipina magdalo ':
   
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 6: The original national anthem composed by?:')
    if answer.lower()=='julian felipe':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
        
    answer=input('Question 7: he was mastermind of the revolution: ')
    if answer.lower()=='apolinario mabini':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
      
    answer=input('Question 8: he was captured emilio Aguinaldo with the help of macaabebe: ')
    if answer.lower()=='General Frederick':
   
        score += 3
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 9: The original national anthem composed by?:')
    if answer.lower()=='emilio aguinaldo shrine':
        score += 2
        print('correct')
    else:
        print('Wrong Answer :(')
        
        answer=input('Question 10: he was the first to give the name ‘Felipinas’ in honor of the Spanish crown prince Don Felipe, later to be King Felipe II?: ')
    if answer.lower()=='ruy lopez':
   
        score += 3
        print('correct')
    else:
        print('Wrong Answer :(')
        
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print(" ")
if mark=='50':
	print('you pass')
else:
	print('try againt')
print(greetings.center(60,'-'))