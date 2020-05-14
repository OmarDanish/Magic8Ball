import  time 
import random
i=1

while i >= 1:
    user_question=input("Ask a question, the Magic 8-Ball will answer:\n")
    \
    print ("The 8-Ball is thinking...\n")
    time.sleep(2)
    
    answers=["Yes", 'No', 'Definitely', 'Definitely not', 'I dont know', 'I was not designed for such a complex question', 'Who knows?', 'For sure', 'Dont get your hopes up']
    
    print(random.choice(answers))
    
    time.sleep(2)
    
    play_again=input('Do you want to ask the 8-Ball another question?\n')
    \
    if play_again == "Yes" or "yes":
        i += 1
    elif play_again == "No" or "no":
        i = 0
else:
     print ('Thank you for using the Magic 8-Ball!')


