def solution():
    # Calculate the number of woodwind players
    woodwinds = 110 / (4 + 2 + 1) * 2  # there are twice as many woodwinds as brass, and the percussion players make up 4 times the number of woodwinds

    # Calculate the number of brass players
    brass = 110 / (4 + 2 + 1)  # the percussion players make up 4 times the number of woodwinds, and there are twice as many woodwinds as brass

    result = brass
    return result

print(solution())