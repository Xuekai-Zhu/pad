def solution():
    # Calculate the total number of oysters and crabs on the first day
    day1_total = 50 + 72

    # Calculate the number of oysters and crabs on the second day
    day2_oysters = 50 / 2
    day2_crabs = 72 * (2/3)

    # Calculate the total number of oysters and crabs on the second day
    day2_total = day2_oysters + day2_crabs

    # Calculate the total number of oysters and crabs counted in both days
    total_count = day1_total + day2_total
    result = total_count
    return result

print(solution())