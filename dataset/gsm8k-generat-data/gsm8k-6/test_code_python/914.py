def solution():
    # Find the number of white birds
    white_birds = 40 + 6

    # Calculate the number of birds that fly away
    flying_birds = 0.5 * (40 + white_birds)

    # Calculate the number of birds remaining
    remaining_birds = 40 + white_birds - flying_birds
    result = remaining_birds
    return result

print(solution())