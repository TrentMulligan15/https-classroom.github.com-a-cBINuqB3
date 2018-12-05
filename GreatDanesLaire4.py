import random
import time 

def displayIntro():
    print("You are on campus and there are zombies running wild.")
    print("You see two escapes. The library and the Campus Center")
    print("The campus center is filled with the hungry survivors on campus")
    print("The libary is empty yet has limited supplies")
    hidingSpot=input('Which hiding place will you choose?(Library or CampusCenter)')
    if hidingSpot == "Library":
        checkSpot()   
 
def choosehidingSpot():
    hidingSpot = ''
    while cave != "Library" and cave != "CampusCenter":
        print('Which hiding place will you choose?(Library or CampusCenter)')

    return hidingSpot

def checkhidingSpot(chosenhidingSpot):
    print("You enter you're hiding spot...")
    time.sleep(2)
    print("It is quiet in here.....too quiet...")
    time.sleep(2)
    Print("You here zombies are attacking downstairs, yet there are supplies down there down there for sure...")
    time.sleep(2)

    hidingSpot = random.randint(1, 2)

    if chosenhidingSpot == str(friendlyCave):
        print('The zombies feast on your flesh')
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()

    hidingSpotNumber = choosehidingSpot()

    checkhidingSpot(hidingSpotNumber)

    print('Do you want to play again?(yes or no)')
    playAgain = input()


    
