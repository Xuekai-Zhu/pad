def solution():
    initial_carrots = 300  # initial number of carrots
    used_before_lunch = (2/5) * initial_carrots  # number of carrots used before lunch
    remaining_carrots = initial_carrots - used_before_lunch  # number of carrots remaining after lunch
    used_after_lunch = (3/5) * remaining_carrots  # number of carrots used after lunch
    carrots_not_used = remaining_carrots - used_after_lunch  # number of carrots not used
    result = carrots_not_used
    return result

print(solution())