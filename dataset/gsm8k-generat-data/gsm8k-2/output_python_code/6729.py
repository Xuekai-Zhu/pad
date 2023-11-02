def solution():
    """A cook had 300 carrots in a bucket he was using to cook meals for a restaurant. Before lunch, he had used 2/5 of the carrots. By the end of the day, he had chopped and used 3/5 of the remaining carrots. How many carrots were not used that day?"""
    initial_carrots = 300
    before_lunch_used = 2/5 * initial_carrots
    remaining_carrots = initial_carrots - before_lunch_used
    end_of_day_used = 3/5 * remaining_carrots
    not_used = remaining_carrots - end_of_day_used
    result = not_used
    return result

print(solution())