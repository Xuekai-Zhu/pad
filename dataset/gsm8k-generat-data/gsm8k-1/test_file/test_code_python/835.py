def solution():
    """A farmer extracts 5 liters of milk a day from a cow. Since he has 3 cows, how many more cows does he need to have to produce 25 liters of milk a day?"""
    milk_per_cow = 5
    current_cows = 3
    desired_milk = 25
    extra_cows_needed = (desired_milk - (current_cows * milk_per_cow)) / milk_per_cow
    result = extra_cows_needed
    return result

print(solution())