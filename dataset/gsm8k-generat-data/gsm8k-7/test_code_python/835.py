def solution():
    front = 100
    back = 2*front
    total = 700
    
    # Calculate the total number of cars that were initially parked
    initial = front + back
    
    # Calculate the number of cars that were parked during the play
    parked_during_play = total - initial
    
    result = parked_during_play
    return result

print(solution())