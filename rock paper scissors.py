#Rock Paper scissors game
print("welcome to rock paper scissors")
import random
import time
cont = True
p1_score = 0
c1_score = 0
while cont:
    p1_choice = input("please input your choice, rock(r), paper(p), scissors(s)")
    if p1_choice in ["r","p","s"]:
        print("good choice!")
        choices = ["r","p","s"]
        c1_choice = random.choice(choices)
        print("computer choosing")
        for x in range(3):
            time.sleep(1)
            print("...")
        print(p1_choice + " vs " + c1_choice)
        if p1_choice == c1_choice:
            print("DRAW!!")
        elif p1_choice=="s" and c1_choice=="p" or p1_choice=="r" and c1_choice=="s" or p1_choice=="p" and c1_choice=="r":
            print("YOU WIN!")
            p1_score += 1
        else:
            print("YOU LOSE!")
            c1_score += 1
        print("player score = " + str(p1_score) + "       computer score = " + str(c1_score))
        print("Press x to quit or another letter to continue")
        playagain = input("")
        if playagain == "x":
            cont = False
        else:
            print("lets play again then")
            time.sleep(1)
            print("")
    else:
        print("you must pick from r/p/s")
if p1_score > c1_score:
    print("""
***********************************************************************************************************************************************
***********************************************************************************************************************************************
WWWWWWWW***************************WWWWWWWWIIIIIIIIIINNNNNNNN********NNNNNNNNNNNNNNNN********NNNNNNNNEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRR***
W::::::W***************************W::::::WI::::::::IN:::::::N*******N::::::NN:::::::N*******N::::::NE::::::::::::::::::::ER::::::::::::::::R**
W::::::W***************************W::::::WI::::::::IN::::::::N******N::::::NN::::::::N******N::::::NE::::::::::::::::::::ER::::::RRRRRR:::::R*
W::::::W***************************W::::::WII::::::IIN:::::::::N*****N::::::NN:::::::::N*****N::::::NEE::::::EEEEEEEEE::::ERR:::::R*****R:::::R
*W:::::W***********WWWWW***********W:::::W***I::::I**N::::::::::N****N::::::NN::::::::::N****N::::::N**E:::::E*******EEEEEE**R::::R*****R:::::R
**W:::::W*********W:::::W*********W:::::W****I::::I**N:::::::::::N***N::::::NN:::::::::::N***N::::::N**E:::::E***************R::::R*****R:::::R
***W:::::W*******W:::::::W*******W:::::W*****I::::I**N:::::::N::::N**N::::::NN:::::::N::::N**N::::::N**E::::::EEEEEEEEEE*****R::::RRRRRR:::::R*
****W:::::W*****W:::::::::W*****W:::::W******I::::I**N::::::N*N::::N*N::::::NN::::::N*N::::N*N::::::N**E:::::::::::::::E*****R:::::::::::::RR**
*****W:::::W***W:::::W:::::W***W:::::W*******I::::I**N::::::N**N::::N:::::::NN::::::N**N::::N:::::::N**E:::::::::::::::E*****R::::RRRRRR:::::R*
******W:::::W*W:::::W*W:::::W*W:::::W********I::::I**N::::::N***N:::::::::::NN::::::N***N:::::::::::N**E::::::EEEEEEEEEE*****R::::R*****R:::::R
*******W:::::W:::::W***W:::::W:::::W*********I::::I**N::::::N****N::::::::::NN::::::N****N::::::::::N**E:::::E***************R::::R*****R:::::R
********W:::::::::W*****W:::::::::W**********I::::I**N::::::N*****N:::::::::NN::::::N*****N:::::::::N**E:::::E*******EEEEEE**R::::R*****R:::::R
*********W:::::::W*******W:::::::W*********II::::::IIN::::::N******N::::::::NN::::::N******N::::::::NEE::::::EEEEEEEE:::::ERR:::::R*****R:::::R
**********W:::::W*********W:::::W**********I::::::::IN::::::N*******N:::::::NN::::::N*******N:::::::NE::::::::::::::::::::ER::::::R*****R:::::R
***********W:::W***********W:::W***********I::::::::IN::::::N********N::::::NN::::::N********N::::::NE::::::::::::::::::::ER::::::R*****R:::::R
************WWW*************WWW************IIIIIIIIIINNNNNNNN*********NNNNNNNNNNNNNNN*********NNNNNNNEEEEEEEEEEEEEEEEEEEEEERRRRRRRR*****RRRRRRR
***********************************************************************************************************************************************
***********************************************************************************************************************************************
***********************************************************************************************************************************************
***********************************************************************************************************************************************
***********************************************************************************************************************************************
***********************************************************************************************************************************************
***********************************************************************************************************************************************
""")
time.sleep(3)
    

        
        
    
