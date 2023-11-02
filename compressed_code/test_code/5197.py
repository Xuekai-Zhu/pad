def solution():
    
    initial_carrots = 300
    before_lunch_used = 2/5 * initial_carrots
    remaining_carrots = initial_carrots - before_lunch_used
    end_of_day_used = 3/5 * remaining_carrots
    not_used = remaining_carrots - end_of_day_used
    result = not_used
    return result

print(solution())