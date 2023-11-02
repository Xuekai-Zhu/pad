def solution():
    """A cook had 300 carrots in a bucket he was using to cook meals for a restaurant. Before lunch, he had used 2/5 of the carrots. By the end of the day, he had chopped and used 3/5 of the remaining carrots. How many carrots were not used that day?"""
    # Define the initial number of carrots
    initial_carrots = 300

    # Calculate the number of carrots used before lunch
    before_lunch = initial_carrots * (2/5)

    # Calculate the number of remaining carrots after lunch
    remaining_carrots = initial_carrots - before_lunch

    # Calculate the number of carrots used by the end of the day
    end_of_day = remaining_carrots * (3/5)

    # Calculate the number of carrots not used that day
    not_used = remaining_carrots - end_of_day

    result = round(not_used)
    return result

print(solution())