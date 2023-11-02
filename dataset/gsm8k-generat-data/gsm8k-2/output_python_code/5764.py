def solution():
    """Lily got a new puppy for her birthday. She was responsible for feeding the puppy 1/4 cup of food three times a day for two weeks starting tomorrow. For the following 2 weeks, Lily will feed him 1/2 cup of food twice a day. She has fed him 1/2 cup of food today. Including today, how much food will the puppy eat over the next 4 weeks?"""
    total_food = 0
    
    # First 2 weeks
    for i in range(0, 14):
        total_food += (1/4) * 3
    
    # Next 2 weeks
    for i in range(0, 14):
        total_food += (1/2) * 2
    
    # Add food from today
    total_food += 0.5
    
    result = total_food
    return result

print(solution())