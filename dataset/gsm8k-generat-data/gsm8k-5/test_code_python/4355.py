def solution():
    # Number of people at the game on Monday
    monday = 80 - 20

    # Number of people at the game on Wednesday
    wednesday = monday + 50

    # Number of people at the game on Friday
    friday = 80 + monday

    # Total number of people at the games for the week
    total = monday + wednesday + friday + 80

    # Calculate the number of people who attended more than expected
    difference = total - 350
    result = difference
    return result

print(solution())