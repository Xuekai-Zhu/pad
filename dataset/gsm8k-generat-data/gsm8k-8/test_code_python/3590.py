def solution():
    total_pages = 354
    first_day = 63
    second_day = 2 * first_day
    third_day = second_day + 10
    
    # Calculate the pages read in the first three days
    pages_read_first_three_days = first_day + second_day + third_day
    
    # Calculate the pages read on the fourth day
    pages_read_fourth_day = total_pages - pages_read_first_three_days
    
    result = pages_read_fourth_day
    return result

print(solution())