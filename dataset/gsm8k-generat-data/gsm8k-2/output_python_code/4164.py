def solution():
    """Paul eats a lot when he studies. He loves sandwiches and eats them at the same rate every three days. He eats 2 sandwiches the first day, then doubles that number of sandwiches for the second day. On the third day, he doubles the number of sandwiches he ate on the second day. How many sandwiches would Paul eat if he studied 6 days in a row?"""
    first_day = 2
    second_day = first_day * 2
    third_day = second_day * 2
    sandwiches_per_cycle = first_day + second_day + third_day
    cycles = 6 // 3
    total_sandwiches = cycles * sandwiches_per_cycle
    remaining_days = 6 % 3
    if remaining_days == 1:
        total_sandwiches += first_day
    elif remaining_days == 2:
        total_sandwiches += first_day + second_day
    result = total_sandwiches
    return result

print(solution())