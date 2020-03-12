"""Start page for my gaming application"""

import random

def welcome():
    for i in range(0, 20):
        print("*\t", end="")
    print()
    print("*", end="")
    for i in range(0, 19):
        print("*\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 19):
        print("*\t", end=" ")
    print("*")
    print("*", end="")
    for i in range(0, 8):
        print("*\t", end="")
    print("WELCOME", end="")
    for i in range(0, 10):
        print("*\t", end="")
    print("*", end="")
    for i in range(0, 19):
        print("*\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 19):
        print("*\t", end="")
    print("*")
    for i in range(0, 20):
        print("*\t", end="")
    print()
    input("Press any key to start:")
    welcome()
    print("\n"*100)

def mainmenu():
    print("1.Rock Paper Scissors\n2.Cows and Bulls\n3.Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        rockpaperscissorsmenu()
    elif ch==2:
        cowsandbullsmenu()
    elif ch==3:
        exit()
    else:
        print("Invalid Choice")
        mainmenu()

def rockpaperscissorsmenu():
    def welcome():
        for i in range(0, 20):
            print("*\t", end="")
        print()

    print("*", end="")
    for i in range(0, 19):
        print("*\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 19):
        print("*\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 8):
        print("*\t", end="")
    print("WELCOME", end="")
    for i in range(0, 10):
        print("*\t", end="")
    print("*", end="")
    for i in range(0, 19):
        print("*\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 19):
        print("*\t", end="")
    print("*")
    for i in range(0, 20):
        print("*\t", end="")
    print()
    input("Press any key to start:")
    welcome()
    print("\n" * 100)

    print("1.Play\n2.Rules\n3.Return to main menu")
    ch = int(input("Enter your choice"))
    if ch==1:
        rockpaperscissors()
    elif ch==2:
        rockpaperscissorsrules()
    elif ch==3:
        mainmenu()
    else:
        print("Invalid Choice")
        rockpaperscissorsmenu()

def cowsandbullsmenu():
    def welcome():
        for i in range(0, 20):
            print("*\t", end="")
        print()

    print("*", end="")
    for i in range(0, 19):
        print("*\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 19):
        print("*\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 8):
        print("*\t", end="")
    print("WELCOME", end="")
    for i in range(0, 10):
        print("*\t", end="")
    print("*", end="")
    for i in range(0, 19):
        print("*\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 19):
        print("*\t", end="")
    print("*")
    for i in range(0, 20):
        print("*\t", end="")
    print()
    input("Press any key to start:")
    welcome()
    print("\n" * 100)

    print("1.Play\n2.Rules\n3.Return to main menu")
    ch = int(input("Enter your choice"))
    if ch==1:
        cowsandbulls()
    elif ch==2:
        cowsandbullsrules()
    elif ch==3:
        mainmenu()
    else:
        print("Invalid Choice")
        cowsandbullsmenu()



def rockpaperscissorsrules():
    print("1.Read the rules\n2.Exit")
    ch = int(input("Enter your choice"))
    if ch==1:
        print("An easily memorised rule determines the winner: “Rock breaks scissors, scissors cuts paper, paper covers rock.” In other words, a player who chooses rock beats one who chooses scissors; scissors in turn beats paper; paper beats rock. This yields a winner whenever the two players choose differently")
    elif ch==2:
        rockpaperscissorsmenu()
    else:
        rockpaperscissorsmenu()



def cowsandbullsrules():
    print("1.Read the rules\n2.Exit")
    ch = int(input("Enter your choice"))
    if ch==1:
        print("On a sheet of paper, the players each write a 4-digit secret number. The digits must be all different. Then, in turn, the players try to guess their opponent's number who gives the number of matches. If the matching digits are in their right positions, they are bulls, if in different positions, they are cows")
    else:
        cowsandbullsmenu()


def rockpaperscissors():
    print("WELCOME TO RCOK PAPERS AND SCISSORS")
    print("You will be competing against the computer. The player that scores 3 points first will be declared as the winner")
    print('If your choice is rock please enter 0')
    print('If your choice is paper please enter 1')
    print('If your choice is scissors please enter 2')
    print("if you want to exit please enter -1")
    user=0
    comp=0
    cnt=0
    choice=["rock","paper","scissors"]
    while(user<5) and (comp<5) and (cnt<10):
        cnt+=1
        user_ch=int(input("Enter your choice "))
        if user_ch==-1:
            print('Thank you')
            break
        comp_ch=random.choice([0,1,2])
        if user_ch==0 and comp_ch==1:
            comp+=1
        elif user_ch==0 and comp_ch==2:
            user+=1
        elif user_ch == 1 and comp_ch == 0:
            user += 1
        elif user_ch == 1 and comp_ch == 2:
            comp += 1
        elif user_ch == 2 and comp_ch == 0:
            comp += 1
        elif user_ch == 2 and comp_ch == 1:
            user += 1
        print("You:", choice[user_ch])
        print("Computer", choice[comp_ch])
        print("Your score:", user, "\t Computer's Score:", comp)
    if (user > comp):
        print("Congragulations!You win!")
    elif (comp > user):
        print("Oops!Sorry you lose. Better luck next time!")
    else:
        print("Match Draw")
    mainmenu()

def cowsandbulls():
    words=["rate","fail","cake","sore","tear","calm","rage","time","face","swan"]
    rand=random.randrange(0,10)
    word=words[rand]
    cnt=0
    while(cnt<15):
        s=input("Enter string:")
        if s=="-1":
            print("Thank you!")
            return
        cows=0
        bulls=0
        #time mite
        chars=0
        for c in s:
            if c in word:
                chars+=1 #chars=4
        for i in range(0,4):
            if s[i]==word[i]:
                bulls+=1 #bulls=2
        cows=chars-bulls
        print("Cows:",cows,"\tBulls:",bulls)
        if bulls==4:
            print("Congragulations!You win!")
            mainmenu()
        cnt+=1
    print("Oops!Maximum guess limit reached!")
    mainmenu()
welcome()
print("\n"*100)
mainmenu()