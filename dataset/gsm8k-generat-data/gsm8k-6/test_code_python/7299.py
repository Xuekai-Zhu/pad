def solution():
    initial_leaves = 340  # initial quantity of leaves
    daily_drop = initial_leaves / 10  # number of leaves dropped each day
    fifth_day_drop = initial_leaves - (daily_drop * 4)  # number of leaves dropped on fifth day
    result = fifth_day_drop
    return result

print(solution())