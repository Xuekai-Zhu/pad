def solution():
    calories_per_chip = 10
    chips_per_bag = 24
    cost_per_bag = 2
    calories_wanted = 480
    cost_of_chips = cost_per_bag * (calories_wanted / calories_per_chip)
    result = cost_of_chips
    return result

print(solution())