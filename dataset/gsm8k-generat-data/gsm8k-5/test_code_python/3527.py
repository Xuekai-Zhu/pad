def solution():
    distance_1 = 10  # Marsha has to drive 10 miles for her first package
    distance_2 = 28  # Marsha has to drive 28 miles for her second package
    distance_3 = distance_2 / 2  # Marsha has to drive half as far for her third package
    total_distance = distance_1 + distance_2 + distance_3  # Total distance Marsha drives in a day
    total_pay = 104  # Marsha gets paid $104 for the day

    # Calculate Marsha's pay per mile driven
    pay_per_mile = total_pay / total_distance
    result = pay_per_mile
    return result

print(solution())