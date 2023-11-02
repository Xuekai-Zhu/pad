def solution():
    # Calculate the total number of oysters and crabs Eric saw in two days
    oysters_day1 = 50
    crabs_day1 = 72
    oysters_day2 = oysters_day1 / 2
    crabs_day2 = (2/3) * crabs_day1
    total_oysters = oysters_day1 + oysters_day2
    total_crabs = crabs_day1 + crabs_day2
    result = total_oysters + total_crabs
    return result

print(solution())