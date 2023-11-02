def solution():
    """Eric has a chicken farm with 4 chickens. His chickens lay 3 eggs each day. If Eric collects all the eggs after 3 days, then how many eggs will Eric have collected?"""
    num_chickens = 4
    eggs_per_day = 3
    num_days = 3
    total_eggs = num_chickens * eggs_per_day * num_days
    result = total_eggs
    return result

print(solution())