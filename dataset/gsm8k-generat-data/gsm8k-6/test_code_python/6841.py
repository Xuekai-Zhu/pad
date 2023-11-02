def solution():
    # Calculate the total number of pills Janet takes in the month
    pills_first_half = (2 + 3) * 14  # two multivitamins and three calcium supplements every day for the first two weeks (14 days)
    pills_second_half = (2 + 1) * 14  # two multivitamins and one calcium supplement every day for the last two weeks (14 days)
    total_pills = pills_first_half + pills_second_half
    result = total_pills
    return result

print(solution())