def solution():
    """Lily got a new puppy for her birthday. She was responsible for feeding the puppy 1/4 cup of food three times a day for two weeks starting tomorrow. For the following 2 weeks, Lily will feed him 1/2 cup of food twice a day. She has fed him 1/2 cup of food today. Including today, how much food will the puppy eat over the next 4 weeks?"""
    initial_cups_per_day = 0.25 * 3
    initial_days = 14
    initial_cups = initial_cups_per_day * initial_days
    
    new_cups_per_day = 0.5 * 2
    new_days = 14
    new_cups = new_cups_per_day * new_days
    
    total_cups = initial_cups + new_cups + 0.5
    
    result = total_cups
    return result

print(solution())