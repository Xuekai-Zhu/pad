def solution():
    current_zombies = 480  # There are 480 zombies currently in the mall
    days_ago = 0  # Initialize the counter for number of days ago

    # Keep doubling the number of zombies until there are less than 50 left
    while current_zombies >= 50:
        days_ago += 1
        current_zombies = current_zombies / 2
    
    result = days_ago
    return result

print(solution())