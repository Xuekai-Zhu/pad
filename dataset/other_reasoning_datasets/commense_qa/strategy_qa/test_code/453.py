def solution():
    college_degree_time = 2 * 365 * 24 # in hours
    bartender_training_time = 40
    if bartender_training_time < college_degree_time:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())