def solution():
    """A cook had 300 carrots in a bucket he was using to cook meals for a restaurant. Before lunch, he had used 2/5 of the carrots. By the end of the day, he had chopped and used 3/5 of the remaining carrots. How many carrots were not used that day?"""
    # Define the total number of carrots
    total_carrots = 300

    # Calculate the number of carrots used before lunch
    used_before_lunch = total_carrots * 2 / 5

    # Calculate the number of carrots remaining after lunch
    remaining_after_lunch = total_carrots - used_before_lunch

    # Calculate the number of carrots used by the end of the day
    used_by_end_of_day = remaining_after_lunch * 3 / 5

    # Calculate the number of carrots not used that day
    not_used = remaining_after_lunch - used_by_end_of_day

    # Display the number of carrots not used
    result = not_used
    return result

print(solution())