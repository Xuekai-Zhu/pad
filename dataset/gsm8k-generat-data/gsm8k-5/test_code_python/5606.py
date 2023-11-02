def solution():
    time_vacuum = 45  # in minutes
    time_dust = 60  # in minutes
    time_mop = 30  # in minutes
    time_brush_each_cat = 5  # in minutes
    num_cats = 3
    total_cleaning_time = time_vacuum + time_dust + time_mop + (num_cats * time_brush_each_cat)

    free_time = 3 * 60  # in minutes
    remaining_time = free_time - total_cleaning_time

    result = remaining_time
    return result

print(solution())