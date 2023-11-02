def solution():
    total_marbles = 63
    
    # Let's assume I have x marbles
    x = 0
    
    # If I give my brother 2 marbles, he will have (x-2) marbles
    brother_marbles = x - 2
    
    # If I have x marbles, my friend will have 3x marbles
    friend_marbles = 3 * x
    
    # If I give my brother 2 marbles, then my total marbles will be (x-2) + x + 3x = 63
    # Solving for x, we get:
    x = (63 + 2 - brother_marbles) / 4
    
    result = x
    return result

print(solution())