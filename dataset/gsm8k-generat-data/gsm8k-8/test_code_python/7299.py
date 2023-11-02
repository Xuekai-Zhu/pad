def solution():
    initial_leaves = 340
    daily_leaves_dropped = initial_leaves / 10

    # Leaves dropped on first four days
    first_four_days = 4 * daily_leaves_dropped

    # Leaves dropped on fifth day
    fifth_day = initial_leaves - first_four_days

    result = fifth_day
    return result

print(solution())