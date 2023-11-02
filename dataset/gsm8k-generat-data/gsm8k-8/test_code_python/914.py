def solution():
    # Calculate the number of white birds
    white_birds = 40 + 6

    # Calculate the total number of birds before any fly away
    total_birds = white_birds + 40

    # Calculate the number of birds that fly away
    flying_birds = total_birds / 2

    # Calculate the number of birds remaining
    remaining_birds = total_birds - flying_birds

    result = remaining_birds
    return result

print(solution())