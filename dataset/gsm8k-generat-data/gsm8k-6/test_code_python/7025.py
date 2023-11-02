def solution():
    # Calculate Voldemort's total caloric intake
    total_cal = 110 + 310 + 215 + 560 + 780  # sum of calories from cake, chips, coke, breakfast, and lunch
    remaining_cal = 2500 - total_cal  # calculate how many calories Voldemort can still consume
    result = remaining_cal
    return result

print(solution())