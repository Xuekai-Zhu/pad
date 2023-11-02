def solution():
    # Define the distances of the three packages
    distance1 = 10
    distance2 = 28
    distance3 = distance2 / 2

    # Calculate the total distance traveled
    total_distance = distance1 + distance2 + distance3

    # Calculate the pay per mile
    pay_per_mile = 104 / total_distance
    result = pay_per_mile
    return result

print(solution())