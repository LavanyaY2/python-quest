#Career test in Python
#Authors: Rana, Jenny, Lavanya
import time
lawyer, architect, accountant, software, entrepreneur, politician, engineer, doctor, actor, teacher = 2, 2, 2, 2, 2, 2, 2, 2, 2, 2
#initialA = [lawyer, architect] 

def career_counter(career, choice):
    if choice == 1:
        career -= 1
    elif choice == 2:
        career += 0
    elif choice == 3:
        career +=1
    return career
def main():
    print("************************************************************")
    print("                 WELCOME TO THE CAREER TEST                  ")
    print("************************************************************")
    time.sleep(2)

    print("We'll be asking you a series of questions to determine\nYour future career!\n\n")
    name = input("Enter your name: ")
    
    # lawyer 1
    print("Do you like debates and the art of arguing?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    lawyerFinal = career_counter(lawyer, answer)
    
    # architect 1
    print("Do you like to plan or design structures?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    architectFinal = career_counter(architect, answer)
    
    # accountant 1
    print("Is data-entry and analyzing mathematical figures something you enjoy doing?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    accountantFinal = career_counter(accountant, answer)

    # software 1
    print("Are you passionate about software technology?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    softwareFinal = career_counter(software, answer)

    #lawyer 2
    print("Does studying and analyzing the laws and regulations to determine consequences for legal cases sound appealing to you?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    lawyerFinal = career_counter(lawyer, answer)

    #entrepreneur 1
    print("Do you see yourself collaborating with board members to discuss issues and resolve problems?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    entrepreneurFinal = career_counter(entrepreneur, answer)

    #engineer 1
    print("Do you enjoy hands-on learning opportunities in STEM?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    engFinal = career_counter(engineer, answer)

    #politician 1
    print("Do you enjoy public speaking about important political issues?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    politiicanFinal = career_counter(politician, answer)

    #actor 1
    print("Would you enjoy working closely with directors, writers, and other actors to find a suitable interpretation of a role?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    actFinal = career_counter(actor, answer)

    #software 2 
    print("Is coding and building versatile applications something you would enjoy pursuing?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    softwareFinal = career_counter(software, answer)
    
    #actor 2
    print("Would you like to attend auditions and casting calls for roles?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    actFinal = career_counter(actor, answer)

    # Doctor 1
    print("Is biology one of your major subjects of interest?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    doctorFinal = career_counter(doctor, answer)

    # Engineer 2
    print("Does the idea of applying your physics and chemistry knowledge into building machinery and systems excite you?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    engFinal = career_counter(engineer, answer)
    
    #accountant 2 
    print("Do you see yourself working in an office environment?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    accountantFinal = career_counter(accountant, answer)
    
# Doctor 2
    print("Would you like to perform and interpret tests and analyze reports to diagnose a patient’s condition?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    doctorFinal = career_counter(doctor, answer)

#entrepreneur 2
    print("Does the idea of brainstorming innovative business ideas excite you?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    entrepreneurFinal = career_counter(entrepreneur, answer)

# Teacher 1

    print("Do you see yourself working with kids in the future?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    teacherFinal = career_counter(teacher, answer)
  #architect 2
    print("Would you like to integrate engineering concepts into architectural designs?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    architectFinal = career_counter(architect, answer)

# Teacher 2    
    print("Does the idea of becoming a mentor resonate with youture?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    teacherFinal = career_counter(teacher, answer)


#politician  print("Would you say you possess the qualities of a good leader?\n1. Disagree\n2. Neutral\n3. Agree")
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    politicianFinal = career_counter(politician, answer)


    finalArray = [teacherFinal, politicianFinal, lawyerFinal, engFinal, softwareFinal, entrepreneurFinal,doctorFinal, accountantFinal, actFinal, architectFinal]
    finalArray.sort(reverse = True)
    print(name, finalArray)
    


main()

