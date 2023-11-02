def solution():
    num_tables = 4
    legs_per_table = 4
    screws_per_leg = 2
    total_legs = num_tables * legs_per_table
    total_screws = 40

    # Calculate the total number of screws needed
    total_screws_needed = total_legs * screws_per_leg

    # Calculate the number of screws left over
    screws_left_over = total_screws - total_screws_needed
    result = screws_left_over
    return result

print(solution())