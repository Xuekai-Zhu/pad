def solution():
    monday_pots = 12
    tuesday_pots = monday_pots * 2

    # The total number of pots created on Monday and Tuesday
    total_pots = monday_pots + tuesday_pots

    # The number of pots created on Wednesday is the difference between the total and 50
    wednesday_pots = 50 - total_pots

    result = wednesday_pots
    return result

print(solution())