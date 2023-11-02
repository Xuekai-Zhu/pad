def solution():
    """A cook had 300 carrots in a bucket he was using to cook meals for a restaurant. Before lunch, he had used 2/5 of the carrots. By the end of the day, he had chopped and used 3/5 of the remaining carrots. How many carrots were not used that day?"""
    total_carrots = 300
    used_before_lunch = 2/5 * total_carrots
    remaining_carrots = total_carrots - used_before_lunch
    used_after_lunch = 3/5 * remaining_carrots
    unused_carrots = remaining_carrots - used_after_lunch
    result = unused_carrots
    return result

print(solution())