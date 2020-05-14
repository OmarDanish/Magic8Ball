print ("    ")
\

import  time 
import random
check=True

while check:
    user_question=input("Ask a question, the Magic 8-Ball will answer:\n")
    \
    print ("The 8-Ball is thinking...\n")
    time.sleep(2)
    
    answers=["Yes", 'No', 'Definitely', 'Definitely not', 'I dont know', 'I was not designed for such a complex question', 'Who knows?', 'For sure', 'Dont get your hopes up']
    
    print(random.choice(answers))
    \
    time.sleep(2)
    
    play_again=input('Do you want to ask the 8-Ball another question?\n')
    play_again.lower()
    \
    if play_again == "yes":
        check=True
    elif play_again == "no":
        check=False

print ('\nThank you for using the Magic 8-Ball!')
