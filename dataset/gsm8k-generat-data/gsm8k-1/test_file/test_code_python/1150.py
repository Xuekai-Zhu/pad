def solution():
    """Mason likes eating carrots. If he eats 4 carrots each on weekdays and 5 carrots each on Saturday and Sunday, how many carrots does he eat a week?"""
    carrots_weekdays = 4
    carrots_weekend = 5
    total_carrots = (carrots_weekdays * 5) + (carrots_weekend * 2)
    result = total_carrots
    return result

print(solution())