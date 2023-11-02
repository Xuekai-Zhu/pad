def solution():
    initial_oysters = 50
    initial_crabs = 72

    # Calculate the number of oysters counted on the second day
    second_day_oysters = initial_oysters / 2

    # Calculate the number of crabs counted on the second day
    second_day_crabs = initial_crabs * 2 / 3

    # Calculate the total number of oysters and crabs counted over the two days
    total_count = initial_oysters + second_day_oysters + initial_crabs + second_day_crabs

    result = total_count
    return result

print(solution())