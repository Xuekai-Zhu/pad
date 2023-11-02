def solution():
    
    dozens_bought = 3
    pieces_bought = dozens_bought * 12 + 10
    pieces_left_over = 15
    pieces_eaten = pieces_bought - pieces_left_over
    result = pieces_eaten
    return result

print(solution())