def solution():
    cal_per_chip = 10
    chips_per_bag = 24
    cost_per_bag = 2.0
    calories_needed = 480

    # Calculate the number of bags needed to eat desired number of calories
    num_bags_needed = calories_needed / (cal_per_chip * chips_per_bag)

    # Calculate the cost of the bags of chips needed
    cost_needed = num_bags_needed * cost_per_bag
    result = cost_needed
    return result

print(solution())