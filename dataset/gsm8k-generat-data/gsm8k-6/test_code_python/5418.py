def solution():
    zombies = 480  # starting number of zombies
    days_ago = 0  # initialize the number of days ago
    while zombies >= 50:  # loop until there are less than 50 zombies
        zombies //= 2  # divide the number of zombies by 2 (i.e., double the number of days ago)
        days_ago += 1  # increment the number of days ago
    result = days_ago
    return result

print(solution())