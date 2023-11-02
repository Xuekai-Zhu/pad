def solution():
    """Nate's dog can dig six holes a day. He digs for 14 days while Nate is on vacation. When Nate gets home, he starts filling in 9 holes a day, but the dog keeps digging 6 new holes every night. How many weeks does it take him to fill in all the holes?"""
    initial_dug_holes = 6 * 14
    new_holes_dug_per_day = 6
    holes_filled_per_day = 9
    net_holes_filled_per_day = holes_filled_per_day - new_holes_dug_per_day
    remaining_holes = initial_dug_holes
    days_to_fill_holes = 0
    while remaining_holes > 0:
        remaining_holes -= net_holes_filled_per_day
        days_to_fill_holes += 1
        remaining_holes += new_holes_dug_per_day
    result = days_to_fill_holes / 7
    return result

print(solution())