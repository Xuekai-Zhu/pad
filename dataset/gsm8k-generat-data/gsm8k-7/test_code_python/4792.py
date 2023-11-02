def solution():
    monday_pots = 12
    tuesday_pots = 2 * monday_pots
    total_pots = monday_pots + tuesday_pots + 50

    # Calculate the number of pots created on Wednesday
    wednesday_pots = total_pots - monday_pots - tuesday_pots
    result = wednesday_pots
    return result

print(solution())