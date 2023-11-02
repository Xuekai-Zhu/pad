def solution():
    # Calculate the number of units occupied in the building for the year
    occupied_units = (3/4) * 100 * 12  # 3/4 occupied for a whole year

    # Calculate the total amount of rent Mr. Maximilian receives in the year
    total_rent = occupied_units * 400  # each resident pays a rent of $400

    result = total_rent
    return result

print(solution())