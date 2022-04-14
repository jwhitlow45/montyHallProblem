import random

def main():
    numRounds = [10,100,1000,10000,100000,1000000]
    numDoorsList = [3,6,9,20,100]
    playerSwitchList = [False, True]
    openWinningDoorList = [False, True]
    
    lines = []
    header = 'rounds,num doors,switch policy,winning door policy,wins,win %\n'
    lines.append(header)
    for rounds in numRounds:
        print(rounds)
        for numDoors in numDoorsList:
            for playerSwitch in  playerSwitchList:
                for openWinningDoor in openWinningDoorList:
                    wins = 0
                    for i in range(rounds):
                        if game_round(numDoors, playerSwitch, openWinningDoor):
                            wins += 1
                            
                    # store result to be saved
                    line = f'{rounds},{numDoors},{playerSwitch},{openWinningDoor},{wins},{wins/rounds}\n'
                    lines.append(line)
                
    with open('montyhallresult.csv', 'w') as FILE:
        FILE.writelines(lines)    
    
def game_round(numDoors: int, isPlayerSwitch: bool, isOpenWinningDoor: bool) -> bool:
    """play a round of the monty hall game

    Args:
        numDoors (int): number of doors in experiment
        isPlayerSwitch (bool): will player switch doors
        isOpenWinningDoor (bool): can the winning door be opened by monty

    Returns:
        bool: True if player wins, false if they Lose
    """
    # winning door and player door are both randomly selected
    winningDoor = random.randint(0, numDoors - 1)
    playerDoor = random.randint(0, numDoors - 1)
    
    # random door is opened (winning)
    if isOpenWinningDoor:
        # cant open player door
        removedDoors = 1
        unopenedDoor = random.randint(0, numDoors - 1)
        if unopenedDoor >= playerDoor:
            unopenedDoor += 1
        
        # if winning door is revealed player wins
        if unopenedDoor != winningDoor and playerDoor != winningDoor:
            return True
    else:
        # cant open player door or winning door, but if they are the same door
        # then only 1 door cannot be opened
        if playerDoor == winningDoor:
            removedDoors = 1
            unopenedDoor = random.randint(0, numDoors - removedDoors)
            if unopenedDoor >= playerDoor:
                unopenedDoor += 1
        else:
            removedDoors = 2
            unopenedDoor = random.randint(0, numDoors - removedDoors)
            if unopenedDoor >= playerDoor:
                unopenedDoor +=1
            if unopenedDoor >= winningDoor:
                unopenedDoor += 1
    
    # switch player door if policy says to do so            
    if isPlayerSwitch:
        playerDoor = unopenedDoor
        
    # player wins if they selected winning door
    return playerDoor == winningDoor
        
        
            
    
            
    
    
    
    
    
    
if __name__ == '__main__':
    main()