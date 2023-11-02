def solution():
    """A frog lays her eggs over a series of 4 days. The first day she lays 50 eggs. The second day, she doubles her production of eggs. The third day she lays 20 more than the second day, and the last day she doubles the first three days total. How many eggs did the frog lay over the span of the 4 days?"""
    first_day = 50
    second_day = 2 * first_day
    third_day = second_day + 20
    total_first_three_days = first_day + second_day + third_day
    fourth_day = 2 * total_first_three_days
    total_eggs = first_day + second_day + third_day + fourth_day
    result = total_eggs
    return result

print(solution())