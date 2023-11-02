def solution():
    num_leaves = 30
    num_bugs = 20
    num_days = 10

    # Calculate the total number of items Carla needs to collect
    total_items = num_leaves + num_bugs

    # Calculate the number of items Carla needs to collect each day
    items_per_day = total_items / num_days
    result = items_per_day
    return result

print(solution())