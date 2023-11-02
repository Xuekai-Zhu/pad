def solution():
    candy_collected = 68
    candy_eaten = 4
    
    # Calculate the total number of candy eaten by both Travis and his brother
    total_candy_eaten = candy_eaten * 2

    # Calculate the number of candy left
    candy_left = candy_collected - total_candy_eaten
    result = candy_left
    return result

print(solution())