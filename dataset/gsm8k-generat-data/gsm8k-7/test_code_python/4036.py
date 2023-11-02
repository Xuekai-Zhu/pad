def solution():
    num_cakes = 320
    day_six = 1  # Number of cakes made on Day 6
    for i in range(6):
        day_six *= 2  # Double the number from the previous day
    # Solve for the number of cakes made on Day 1
    num_cakes_day_one = day_six / 32
    result = num_cakes_day_one
    return result

print(solution())