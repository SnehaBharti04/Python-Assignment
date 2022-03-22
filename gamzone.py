import random
def snake_ladder():
  user_pos=0
  comp_pos=0

  snakes={
      97:78,
      95:56,
      88:24,
      62:18,
      48:26,
      36:6,
      32:10
  }
  ladders={
      2:38,
      4:14,
      8:30,
      28:76,
      21:42,
      50:67,
      71:92,
      80:99
  }
  while user_pos<100 and comp_pos<100:
    choice=int(input("Enter 1 to throw dice\n"))
    if choice==1:
      user_dice=random.randint(1,6)
      if 100-user_pos<user_dice:
        print("Waste move\n")

        comp_dice=random.randint(1,6)
        if 100-comp_pos<comp_dice:
          continue
        comp_pos+=comp_dice
        if comp_pos in snakes.keys():
          comp_pos=snakes[comp_pos]
        if comp_pos in ladders.keys():
          comp_pos=ladders[comp_pos]
        print("Computer is on ",comp_pos)
        continue

      print("dice number is ",user_dice)
      user_pos+=user_dice
      if user_pos in snakes.keys():
        print("Snake bite, dropped from ",user_pos," to ",snakes[user_pos])
        user_pos=snakes[user_pos]
      if user_pos in ladders.keys():
        print("Got ladder from ",user_pos," to ",ladders[user_pos])
        user_pos=ladders[user_pos]
      print("Your current position is ",user_pos)

      comp_dice=random.randint(1,6)
      if 100-comp_pos<comp_dice:
        continue
      comp_pos+=comp_dice
      if comp_pos in snakes.keys():
        comp_pos=snakes[comp_pos]
      if comp_pos in ladders.keys():
        comp_pos=ladders[comp_pos]
      print("Computer is on ",comp_pos)
    
  if user_pos==100:
    print("Winner.....")
    return True
  else:
    print("Sorry Bro...")
    return False


def rps():
  print("Welcome to Rock Paper Scissor...")
 
  while True:
    print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
    choice = int(input("User turn: "))
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")
    comp_choice = random.randint(1, 3)
     
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
 
   
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'
         
    print("Computer choice is: " + comp_choice_name)
 
    print(choice_name + " V/s " + comp_choice_name)
 
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )):
        print("paper wins => ", end = "")
        result = "paper"
         
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)):
        print("Rock wins =>", end = "")
        result = "Rock"
    else:
        print("scissor wins =>", end = "")
        result = "scissor"
 
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
         
    print("Do you want to play again? (Y/N)")
    ans = input()

    if ans == 'n' or ans == 'N':
        break
  print("\nThanks for playing")

def Movie_Guess():
 movie_name=["jercy","gangubai","sholey","pushpa"]
 movie=random.choice(movie_name)
 movie=movie.lower()
 movie.replace(" ","")
 print(movie)
 ans=[]
 for i in range(len(movie)):
    ans.append("*")
 print(ans)
 counter=0
 chance=3
 while counter<len(movie) and chance>0:
    ch=input("Guess Character :")
    flag=False
    for j in range(len(movie)):
      if ch==movie[j]:
        ans[j]=ch
        counter=counter+1
        print(ans)
        flag=True
    if(flag==False):
      chance=chance-1
      print("You guessed Wrong, remaining chances :",chance)

 if chance<=0:
    print("Sorry Bro...")
    return False
 else:
    print("Its..Congratulation...")
    return True

def flames():
  n1=input("Enter your name : ").upper()
  n2=input("Enter second name : ").upper()
  name=n1+n2

  for i in name:
    if name.count(i)!=1:
      name=name.replace(i,"")
  print("FLAMES")
  print("F = Friend \nL = Love \nA = Affection \nM = Marriage \nE = Enemy \nS = Siblings \n\n")
  num=len(name)%6

  r=""
  if num==1:
    r+="Friends"
  elif num==2:
    r+="Love"
  elif num==3:
    r+="Affection"
  elif num==4:
    r+="Marriage"
  elif num==5:
    r+="Enemy"
  elif num==0:
    r+="Siblings"

  print("Relationship is : " ,r)


print("Welcome to GAME ZONE and CANTEEN.....")
points=500
while points>0:
    choice=int(input("\n1 Play Game\n2 Buy from Cafe\n3 Exit\n"))
    if choice==1:
        if points<30:
            print("You dont have money")
        else:
            points=points-30
            game_choice=int(input("\n1 Movie Guess Game \n2 Rock Paper \n3 Snake and Ladder & Scissor\n4 FLAMES\n"))

            if game_choice==1:
              if Movie_Guess():
                points+=20

            elif game_choice==2:
              if rps():
                points+=20

            elif game_choice==3:
              if snake_ladder():
                points+=20

            elif game_choice==4:
              flames()

            else:
              print("Your input is Invalid")

            print("The balance is ",points)

    elif choice==2:
        menu=int(input("MENU :\n1.Vadapav : 30\n2.Panipuri : 40\n3.Dabeli : 60\n"))
        if menu==1:
          if points<70:
            print("You dont have enough money")
          else:
            points=points-30
            print("You bought Vadapav , Balance is ",points)

        elif menu==2:
          if points<60:
            print("Dont have enough money")
          else:
            points=points-40
            print("You bought Panipuri , Balance is ",points)

        elif menu==3:
          if points<50:
            print("You dont have enough money")
          else:
            points=points-60
            print("You bought Dabeli , Balance is ",points)
        else:
            print("Invalid Input")

    elif choice==3:
        break
    else:
        print("Invalid Input")
