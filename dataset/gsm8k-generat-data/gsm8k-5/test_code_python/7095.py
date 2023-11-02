def solution():
    # Calculate the number of oysters and crabs Eric saw on the first day
    oysters_day_1 = 50
    crabs_day_1 = 72

    # Calculate the number of oysters and crabs Eric saw on the second day
    oysters_day_2 = oysters_day_1 / 2
    crabs_day_2 = (2/3) * crabs_day_1

    # Calculate the total number of oysters and crabs Eric saw in two days
    total_oysters = oysters_day_1 + oysters_day_2
    total_crabs = crabs_day_1 + crabs_day_2
    result = total_oysters + total_crabs
    return result

print(solution())