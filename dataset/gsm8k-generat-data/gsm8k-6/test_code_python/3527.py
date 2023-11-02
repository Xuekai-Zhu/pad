def solution():
    # Calculate the total distance Marsha drives
    total_distance = 10 + 28 + (1/2)*28  # Marsha drives 10 miles for her first package, 28 miles for her second package, and half that distance (14 miles) for her third package

    # Calculate Marsha's pay per mile
    pay_per_mile = 104 / total_distance
    result = pay_per_mile
    return result

print(solution())