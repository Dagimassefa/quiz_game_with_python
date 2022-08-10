Programming_questions={
   "1. What is Encapsulation? ":"C",
   "2. A PHP scripting block always starts with___________ and ends with ___________ respectively. : ":"D",
   "3. What does it mean by a Loosely Typed Language? ":"A",
   "4. How do you end an If block in shell scripting? ":"D",
   "5. Java compiles to _______________ that is interpreted at runtime by the underlying  JVM. ":"A"
}
Programming_options=[["A.Allows program code to have different meaning or functions","B.Away to form new classes from existing classes",
"C.The process of keeping classes private so they can not be modified by external codes","D.All of the above"],
["A.<?php and />","B.<php and /php>","C.<?php and >","D.<?php and ?>"],
["A.Programming language that does not require a variable to be defined","B.Programming language that is easy to learn",
"C.Programming language that does'nt have a GUI.","D.All of the above"],
["A.if","B.END","C.esac","D.fi"],
["A.Bytecode","B.Machine Code","C.Human language","D.None"]
]

Networking_questions={
    "1. Which of the OSI model layer made Application layer of DOD model?":"B",
    "2. Which of the following is a feature of TCP model?":"D",
    "3. Class C IP addresses are in s range between____________.":"D",
    "4. What is the subnetwork address if the destination address is 200.45.34.56 and the subnet mask is 255.255.240.0?":"A",
    "5. What is the function of ARP?":"C"
}
Networking_options=[["A.Application,Presentation and Transport","B.Application,Presentation and Session",
"C.Application,Session and Network","D.Application,Session and Data Link"],
["A.Network layer protocol","B.Packetized","C.Delivery not guaranteed","D.Guaranteed packet delivery"],
["A.10.0.0.0—10.255.255.255","B.172.16.0.0—172.31.255.255","C.170.16.0.0—172.31.255.255","D.192.0.0.0-223.255.255.0"],
["A.200.45.32.0","B.210.45.32.0","C.192.45.32.0","D.173.45.32.0"],
["A. responsible for reporting errors and messages","B.allows several networks to work virtually as one LAN.",
"C.responsible for finding a map to any local physical address that IP may request.","D.None"]
]
Security_questions={
    "1. The Metasploit tool is primarily used in which phase of ethical hacking?":"C",
    "2. System misconfiguration is a vulnerability that can be exploited.":"B",
    "3. Which type of hackers use the existing tools and codes for hacking purpose?":"D",
    "4. Why should a Hacker know programming?":"C",
    "5. Which tool is vulnerability scanner?":"A"
}
Security_options=[["A. Reconnaissance","B.Gaining Access","C.Maintaining Access","D.Clearing tracks"],
["A.False","B.True"],
["A.Grey hat","B.Hacktivist","C.Nation sponsored hacker","D.Script kiddies"],
["A.To create application","B.To create website","C.To develop scripts"],
["A.Nessus","B.NMAP","C.Wireshark "]
]
Movie_questions={
    "1. What is the highest grossing movie of all time?":" C",
    "2. What is the name of the secret agency that policies aliens disguised as humans in the film starring will smith and tommy lee jones?":"B",
    "3. What color pill Does Neo take in the matrix?":"A",
    "4. What animal is Alex in Madagascar?":"D",
    "5. What is the name of joey’s character in the commercial for opening milk cartones?":"C"
}
Movie_options=[["A.Avengers: Endgame","B.Titanic","C.Avatar","D.Gone with the wind"],
["A.Alien Agency","B.Men in Black","C.Gemini Men","D.Bad Boys"],
["A.Red","B.Blue","C.Black","D.Orange"],
["A.Hippo","B.Giraffe","C.Zebra","D.Lion"],
["A.Mike","B.Tommy","C.Kevin","D.Drake"]
]
General_knowledge_questions={
    "1. Which of the following is used in pencils?":"A",
    "2. What Galileo invented?":"D",
    "3. Who is the English physicist responsible for the big bang theory?":"C",
    "4. Who among the following invented small pox vaccine?":"B",
    "5. When was World War 1?":"D"
}
General_knowledge_options=[["A.Graphite","B.Silicon","C,Charcoal","D.Phosphorous"],
["A.Barometer","B.Pendulum clock","C.Microscope","D.Thermometer"],
["A.Albert Einstein","B.Michael Skube","C.George Gamow","D.Roger Penrose"],
["A.Robert Koch","B.Edward Jenner","C.Robert Hooke","D.Louis Pasteur"],
["A.1934","B.1944","C.1904","D.1914"]
]
def menu():
    print("================================================================================================================================")
    print("================================================================================================================================")
    print("================================================================================================================================")
    print("================================================================================================================================")
    print("================================================================================================================================")
    print("================================================================================================================================")
    print("================================================================================================================================")
    print("================================================================================================================================")
    print("\t \t \t \t \t PLEASE SELECT A TOPIC")
    print("\t \t \t 1.Programming/Coding questions")
    print("\t \t \t 2.Networking questions")
    print("\t \t \t 3.Cyber Security questions")
    print("\t \t \t 4.Movie questions")
    print("\t \t \t 5.General knowledge questions")
    print("================================================================================================================================")
    print("================================================================================================================================")
    print("================================================================================================================================")
    print("================================================================================================================================")
    print("================================================================================================================================")
    print("================================================================================================================================")
    print("================================================================================================================================")
    print("================================================================================================================================")
    user_choice=int(input("\t \t Please enter a number which correspondes to your choice: "))
    
    print("\t \t \t \t \t PLEASE SELECT A TOPIC")
    if user_choice==1:
        guesses  = []
        correct_guesses=0
        question_num=1
        def check_answer(answer,guess):
            if answer==guess:
                print("Guess")
                return 1
            else:
                print("Incorrect!")
                return 0
        def display_score(correct_guesses,guesses):
            print("----------------------------------------------")
            print("RESULTS")
            print("----------------------------------------------")
            print("Answers: ",end="")
            for i in Programming_questions:
                print(Programming_questions.get(i),end=" ")
            print()
            print("Guesses: ",end="")
            for i in guesses:
                print(i,end=" ")
            print()
            score=float((correct_guesses/len(Programming_questions))*100)
            print("Your score is "+str(score)+"%")
    
        for key in Programming_questions:
            print("--------------------------------------------")
            print(key)
            for i in Programming_options[question_num-1]:
                print(i)
            guess=input("please enter(A,B,C or D):").upper()
            guesses.append(guess)
        # print(guesses)
            correct_guesses+=check_answer(Programming_questions.get(key),guess)
            question_num+=1
        display_score(correct_guesses,guesses)

    elif user_choice==2:
        guesses  = []
        correct_guesses=0
        question_num=1
        def check_answer(answer,guess):
            if answer==guess:
                print("Guess")
                return 1
            else:
                print("Incorrect!")
                return 0
        def display_score(correct_guesses,guesses):
            print("----------------------------------------------")
            print("RESULTS")
            print("----------------------------------------------")
            print("Answers: ",end="")
            for i in Networking_questions:
                print(Networking_questions.get(i),end=" ")
            print()
            print("Guesses: ",end="")
            for i in guesses:
                print(i,end=" ")
            print()
            score=float((correct_guesses/len(Networking_questions))*100)
            print("Your score is "+str(score)+"%")
    
        for key in Networking_questions:
            print("--------------------------------------------")
            print(key)
            for i in Networking_options[question_num-1]:
                print(i)
            guess=input("please enter(A,B,C or D):").upper()
            guesses.append(guess)
        # print(guesses)
            correct_guesses+=check_answer(Networking_questions.get(key),guess)
            question_num+=1
        display_score(correct_guesses,guesses)
    elif user_choice==3:
        guesses  = []
        correct_guesses=0
        question_num=1
        def check_answer(answer,guess):
            if answer==guess:
                print("Guess")
                return 1
            else:
                print("Incorrect!")
                return 0
        def display_score(correct_guesses,guesses):
            print("----------------------------------------------")
            print("RESULTS")
            print("----------------------------------------------")
            print("Answers: ",end="")
            for i in Security_questions:
                print(Security_questions.get(i),end=" ")
            print()
            print("Guesses: ",end="")
            for i in guesses:
                print(i,end=" ")
            print()
            score=float((correct_guesses/len(Security_questions))*100)
            print("Your score is "+str(score)+"%")
    
        for key in Security_questions:
            print("--------------------------------------------")
            print(key)
            for i in Security_options[question_num-1]:
                print(i)
            guess=input("please enter(A,B,C or D):").upper()
            guesses.append(guess)
        # print(guesses)
            correct_guesses+=check_answer(Security_questions.get(key),guess)
            question_num+=1
        display_score(correct_guesses,guesses)
    elif user_choice==4:
        guesses  = []
        correct_guesses=0
        question_num=1
        def check_answer(answer,guess):
            if answer==guess:
                print("Guess")
                return 1
            else:
                print("Incorrect!")
                return 0
        def display_score(correct_guesses,guesses):
            print("----------------------------------------------")
            print("RESULTS")
            print("----------------------------------------------")
            print("Answers: ",end="")
            for i in Movie_questions:
                print(Movie_questions.get(i),end=" ")
            print()
            print("Guesses: ",end="")
            for i in guesses:
                print(i,end=" ")
            print()
            score=float((correct_guesses/len(Movie_questions))*100)
            print("Your score is "+str(score)+"%")
    
        for key in Movie_questions:
            print("--------------------------------------------")
            print(key)
            for i in Movie_options[question_num-1]:
                print(i)
            guess=input("please enter(A,B,C or D):").upper()
            guesses.append(guess)
        # print(guesses)
            correct_guesses+=check_answer(Movie_questions.get(key),guess)
            question_num+=1
        display_score(correct_guesses,guesses)
    elif user_choice==5:
        guesses  = []
        correct_guesses=0
        question_num=1
        def check_answer(answer,guess):
            if answer==guess:
                print("Guess")
                return 1
            else:
                print("Incorrect!")
                return 0
        def display_score(correct_guesses,guesses):
            print("----------------------------------------------")
            print("RESULTS")
            print("----------------------------------------------")
            print("Answers: ",end="")
            for i in General_knowledge_questions:
                print(General_knowledge_questions.get(i),end=" ")
            print()
            print("Guesses: ",end="")
            for i in guesses:
                print(i,end=" ")
            print()
            score=float((correct_guesses/len(General_knowledge_questions))*100)
            print("Your score is "+str(score)+"%")
    
        for key in General_knowledge_questions:
            print("--------------------------------------------")
            print(key)
            for i in General_knowledge_options[question_num-1]:
                print(i)
            guess=input("please enter(A,B,C or D):").upper()
            guesses.append(guess)
        # print(guesses)
            correct_guesses+=check_answer(General_knowledge_questions.get(key),guess)
            question_num+=1
        display_score(correct_guesses,guesses)
    
def play_again():
    response=input("Do you want to play again? (Yes or No):").upper()
    if response=="YES":
        return True
    else:
        return False

menu()
while play_again():
    menu()
print("You are really good see you soon:)")


    



        
