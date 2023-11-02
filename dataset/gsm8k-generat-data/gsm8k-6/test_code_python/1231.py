def solution():
    # Calculate the speed of the first spacecraft
    speed_1 = 2 * 448  # the first spacecraft traveled 448 miles in 0.5 hours

    # Calculate the speed of the second spacecraft
    speed_2 = 2 * 448 / 0.5  # the second spacecraft traveled 448 miles in 1 hour

    # Calculate the difference in speed between the two spacecrafts
    speed_difference = abs(speed_1 - speed_2)

    result = speed_difference
    return result

print(solution())