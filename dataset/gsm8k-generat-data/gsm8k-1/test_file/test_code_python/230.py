def solution():
    """Steve decides to start eating more tomatoes and decides to grows his own cherry tomatoes. He eats twice as much as his girlfriend. He eats 6 per day. If a vine can produce 3 tomatoes per week how many vines does he need?"""
    tomatoes_per_day = 6
    vines_produced_per_week = 3
    total_tomatoes_needed = tomatoes_per_day * 7 * 2  # Steve eats twice as much as his girlfriend, so multiply by 2
    vines_needed = total_tomatoes_needed / vines_produced_per_week

    result = vines_needed
    return result

print(solution())