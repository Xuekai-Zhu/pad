def solution():
    """Sandy's goal is to drink 3 liters of water in a day. She drinks 500 milliliters of water every after 2 hours. After how many hours will she be able to drink a total of 3 liters of water?"""
    
    # Define Sandy's goal and the amount of water she drinks every 2 hours
    goal = 3000
    per_drink = 500
    
    # Initialize the total amount of water drunk and the time passed
    total_water = 0
    time_passed = 0
    
    # Keep drinking until the goal is reached
    while total_water < goal:
        # Drink water and add to the total
        total_water += per_drink
        
        # Increment the time passed by 2 hours
        time_passed += 2
        
    result = time_passed
    return result

print(solution())