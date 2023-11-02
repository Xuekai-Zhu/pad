def solution():
    leaves_needed = 30
    bugs_needed = 20
    days = 10

    # Calculate the total number of items Carla needs to collect
    total_items = leaves_needed + bugs_needed

    # Calculate the daily amount of items Carla needs to collect
    daily_items = total_items / days
    result = daily_items
    return result

print(solution())