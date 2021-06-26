#Career test in Python
#Authors: Rana, Jenny, Lavanya
import time

CBOLD     = '\33[1m'
brightRed = "\033[1;31;40m"
brightGreen = "\033[1;32;40m"
white = "\033[1;37;40m"
CGREYBG    = '\33[100m'

def clearScreen():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

#career counter method calculates counting of each career 
def career_counter(career, choice):
    if choice == 1:
        career = career - 1
    elif choice == 2:
        career = career + 0
    elif choice == 3:
        career = career + 1
    return career

def main():
    clearScreen()
    clearScreen()
    clearScreen()
    clearScreen()
    clearScreen()
    lawyer, architect, accountant, software, entrepreneur, politician, engineer, doctor, actor, teacher = 2, 2, 2, 2, 2, 2, 2, 2, 2, 2
    print("************************************************************")
    print("                 WELCOME TO THE CAREER TEST                  ")
    print("************************************************************")
    time.sleep(2)

    print("We'll be asking you a series of questions to determine\nYour future career!\n\n")
    name = input("Enter your name: ")
    
    # lawyer 1
    print(CBOLD+"\n\nDo you like debates and the art of arguing?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    lawyer = lawyerFinal

    # architect 1
    print(CBOLD+"\nDo you like to plan or design structures?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    architect = architectFinal
    
    # accountant 1
    print(CBOLD+"\nIs data-entry and analyzing mathematical figures something you enjoy doing?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    accountant = accountantFinal

    # software 1
    print(CBOLD+"\nAre you passionate about software technology?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    software = softwareFinal

    #lawyer 2
    print(CBOLD+"\nDoes studying and analyzing the laws and regulations to determine consequences for legal cases sound appealing to you?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    lawyer = lawyerFinal

    #entrepreneur 1
    print(CBOLD+"\nDo you see yourself collaborating with board members to discuss issues and resolve problems?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    entrepreneur = entrepreneurFinal

    #engineer 1
    print(CBOLD+"\nDo you enjoy hands-on learning opportunities in STEM?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    engineer = engFinal

    #politician 1
    print(CBOLD+"\nDo you enjoy public speaking about important political issues?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if(answer >=1 and answer<= 3):
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError:
            print("That is not a valid choice. Please enter a number from 1-3:")

    politicanFinal = career_counter(politician, answer)
    politician = politicanFinal

    #actor 1
    print(CBOLD+"\nWould you enjoy working closely with directors, writers, and other actors to find a suitable interpretation of a role?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    actor = actFinal

    #software 2 
    print(CBOLD+"\nIs coding and building versatile applications something you would enjoy pursuing?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    software = softwareFinal
    
    #actor 2
    print(CBOLD+"\nWould you like to attend auditions and casting calls for roles?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    actor = actFinal

    # Doctor 1
    print(CBOLD+"\nIs biology one of your major subjects of interest?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    doctor = doctorFinal

    # Engineer 2
    print(CBOLD+"\nDoes the idea of applying your physics and chemistry knowledge into building machinery and systems excite you?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    engineer = engFinal
    
    #accountant 2 
    print(CBOLD+"\nDo you see yourself working in an office environment?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    accountant = accountantFinal
    
# Doctor 2
    print(CBOLD+"\nWould you like to perform and interpret tests and analyze reports to diagnose a patient’s condition?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    doctor = doctorFinal

#entrepreneur 2
    print(CBOLD+"\nDoes the idea of brainstorming innovative business ideas excite you?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    entrepreneur = entrepreneurFinal

# Teacher 1
    print(CBOLD+"\nDo you see yourself working with kids in the future?\n\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    teacher = teacherFinal

  #architect 2
    print(CBOLD+"\nWould you like to integrate engineering concepts into architectural designs?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    architect = architectFinal

# Teacher 2    
    print(CBOLD+"\nDoes the idea of becoming a mentor resonate with you?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white)
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
    teacher = teacherFinal
    
    #politician 
    print(CBOLD+"\nWould you say you possess the qualities of a good leader?\n"+brightRed+"1. Disagree\n"+brightRed+ white+ "2. Neutral"+white+brightGreen+"\n3. Agree"+brightGreen+CBOLD + white) 
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
    politician = politicianFinal

    time.sleep(1)
    clearScreen()

    #sorting the array in descending order to find top 3 careers 
    finalArray = [teacherFinal, politicianFinal, lawyerFinal, engFinal, softwareFinal, entrepreneurFinal, doctorFinal, accountantFinal, actFinal, architectFinal]
    stringArray = []
    finalArray.sort(reverse = True)
    
    if (finalArray.index(teacherFinal) < 3): 
        stringArray.append("Teacher")
        
    if (finalArray.index(politicianFinal) < 3):
        stringArray.append("Politician")
        
    if (finalArray.index(engFinal) < 3):
       stringArray.append("Engineer")

    if (finalArray.index(entrepreneurFinal) < 3):
        stringArray.append("Entrepreneur")

    if (finalArray.index(doctorFinal) < 3):
        stringArray.append("Doctor")

    if (finalArray.index(accountantFinal)< 3):
        stringArray.append("Accountant")
    
    if (finalArray.index(lawyerFinal) < 3):
        stringArray.append("Lawyer")

    if (finalArray.index(softwareFinal) < 3):
        stringArray.append("Software Developer")

    if (finalArray.index(actFinal)<3):
        stringArray.append("Actor")
    
    if (finalArray.index(architectFinal) < 3):
        stringArray.append("Architect")
    
    print(CBOLD+"\n"+name + ", your interests spread across multiple fields ! Your top 3 career choices are: \n")
    time.sleep(1)
    print(stringArray[0] + "\n")
    time.sleep(1)
    print(stringArray[1] + "\n")
    time.sleep(1)
    print(stringArray[2] + "\n"+ CBOLD)
    
    
    
main()
