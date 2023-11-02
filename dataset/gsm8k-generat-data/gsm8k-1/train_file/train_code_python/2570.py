def solution():
    """Eric has a chicken farm with 4 chickens. His chickens lay 3 eggs each day. If Eric collects all the eggs after 3 days, then how many eggs will Eric have collected?"""
    chickens = 4
    eggs_per_day = 3
    days = 3
    total_eggs = chickens * eggs_per_day * days
    result = total_eggs
    return result

print(solution())