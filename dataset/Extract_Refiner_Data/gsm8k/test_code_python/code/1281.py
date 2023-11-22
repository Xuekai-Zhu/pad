def solution():
    
    # Define the number of meals distributed to each family
    friday_meals = 64
    saturday_meals = 30
    sunday_meals = 48

    # Calculate the total number of meals distributed
    total_distributed = friday_meals + saturday_meals + sunday_meals

    # Calculate the number of meals left to distribute
    remaining_meals = 1360 - total_distributed

    # Display the number of meals left to distribute
    result = remaining_meals
    return result

print(solution())