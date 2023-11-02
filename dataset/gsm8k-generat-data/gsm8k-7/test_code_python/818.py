def solution():
    clean_house_items = 7
    shower_items = 1
    make_dinner_items = 4
    time_per_item = 10  # minutes

    # Calculate the total time to complete all items
    total_time = (clean_house_items + shower_items + make_dinner_items) * time_per_item

    # Convert total time to hours
    total_time_hours = total_time / 60

    result = total_time_hours
    return result

print(solution())