import random

def main():
    print('hello world')
    
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