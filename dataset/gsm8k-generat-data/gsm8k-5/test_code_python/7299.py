def solution():
    initial_leaves = 340  # The tree had 340 leaves before they started to fall
    daily_fraction = 0.1  # A tenth of the initial quantity of leaves falls every day

    # Calculate the number of leaves that fall each day for the first 4 days
    daily_drop = initial_leaves * daily_fraction
    first_four_days_drop = daily_drop * 4

    # Calculate the number of leaves that drop on the fifth day
    fifth_day_drop = initial_leaves - first_four_days_drop

    result = fifth_day_drop
    return result

print(solution())