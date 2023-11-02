def solution():
    # Calculate the number of white birds
    white_birds = 40 + 6

    # Calculate the total number of birds in the cage
    total_birds = white_birds + 40

    # Calculate the number of birds that flew away
    flew_away = total_birds // 2

    # Calculate the number of birds remaining
    remaining_birds = total_birds - flew_away
    result = remaining_birds
    return result

print(solution())