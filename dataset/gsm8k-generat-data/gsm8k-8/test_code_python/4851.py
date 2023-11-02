def solution():
    # Calculate the original number of each type of silverware
    spoons = 5 + 10
    butter_knives = 5 + 10
    steak_knives = 5 + 10
    forks = 5 + 10

    # Adjust the number of each type of silverware
    spoons -= 4
    butter_knives -= 4
    steak_knives -= 5
    forks -= 3

    # Calculate the total number of silverware pieces
    total = spoons + butter_knives + steak_knives + forks
    result = total
    return result

print(solution())