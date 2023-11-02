def solution():
    # Calculate the number of birds that flew away
    flew_away = 7 - 2  # 2 parrots are left after some flew away, so 5 parrots flew away and the same number of crows flew away

    # Calculate the total number of birds to begin with
    total_birds = 2 + 1 + 5 + flew_away  # 2 parrots and 1 crow are left, plus 5 parrots and flew_away number of crows flew away
    result = total_birds
    return result

print(solution())