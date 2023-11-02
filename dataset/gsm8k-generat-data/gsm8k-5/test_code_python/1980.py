def solution():
    round_bags = 5
    round_per_bag = 20
    long_bags = 4
    long_per_bag = 30

    # Calculate the total number of balloons
    total_balloons = (round_bags * round_per_bag) + (long_bags * long_per_bag)

    # Subtract the number of burst round balloons
    total_balloons -= 5

    result = total_balloons
    return result

print(solution())