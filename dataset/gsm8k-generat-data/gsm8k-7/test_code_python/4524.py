def solution():
    num_oranges = 60
    
    # Johann eats 10 oranges
    num_oranges -= 10
    
    # Half of remaining oranges stolen by Carson
    num_oranges /= 2
    
    # Carson returns 5 oranges
    num_oranges += 5
    
    result = num_oranges
    return result

print(solution())