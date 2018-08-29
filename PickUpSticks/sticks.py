"""
Thomas Manser
Pick up Sticks
Introduction to AI
"""
import random


def AI(moves, current_stick):
    if current_stick == len(moves) - 2:
        pickUp = 1
    else:
        pickUp = random.choice(moves[current_stick])  
    return pickUp

def Player(current_stick, num_sticks):
    if current_stick == num_sticks - 2:
        pickUp = 1
    else:
        pickUp = random.randint(1,3)
    return pickUp

def game(moves, sticks):
    AIturn = False
    current_stick = 0
    moveLog = [0 for x in range(len(sticks))]
    while current_stick <= len(sticks) - 2:
        if AIturn == False:
            current_stick += Player(current_stick, len(sticks))
            AIturn = True
        else:
            moveLog[current_stick] = AI(moves, current_stick)
            current_stick += moveLog[current_stick]
            AIturn = False

    #print("AI won" if AIturn == False else "Player won")
    if AIturn == False:
        for x in range(len(moves)):
            if moveLog[x]:
                moves[x].append(moveLog[x]) 
    return 
    
def main():
    num_sticks = random.randint(10, 100)
    moves = [[1,2,3] for x in range(num_sticks)]
    sticks = [x for x in range(num_sticks, 0, -1)]
    for i in range(1000):
        game(moves, sticks)
    for x in range(len(moves)):
        num_1 = moves[x].count(1)
        num_2 = moves[x].count(2)
        num_3 = moves[x].count(3)

        best_count = max(num_1, num_2, num_3)
        if best_count == num_1:
            best = 1
        elif best_count == num_2:
            best = 2
        else:
            best = 3
        print("The best option for", sticks[x], "number of sticks is", best)

main()

    
