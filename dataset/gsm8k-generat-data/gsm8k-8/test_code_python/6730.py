def solution():
    # Define the initial number of carrots
    initial_carrots = 300

    # Calculate the number of carrots used before lunch
    carrots_before_lunch = initial_carrots * (2/5)

    # Calculate the number of carrots remaining after lunch
    carrots_after_lunch = initial_carrots - carrots_before_lunch

    # Calculate the number of carrots used by the end of the day
    carrots_end_of_day = carrots_after_lunch * (3/5)

    # Calculate the number of carrots not used
    carrots_not_used = carrots_after_lunch - carrots_end_of_day
    result = carrots_not_used
    return result

print(solution())