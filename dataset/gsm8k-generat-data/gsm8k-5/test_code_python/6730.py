def solution():
    total_carrots = 300  # The cook had 300 carrots in the bucket
    used_before_lunch = 2/5 * total_carrots  # The cook used 2/5 of the carrots before lunch
    remaining_carrots = total_carrots - used_before_lunch  # The remaining carrots after lunch
    used_by_end_of_day = 3/5 * remaining_carrots  # The cook used 3/5 of the remaining carrots by end of day
    carrots_not_used = remaining_carrots - used_by_end_of_day  # The number of carrots not used that day
    
    result = carrots_not_used
    return result

print(solution())