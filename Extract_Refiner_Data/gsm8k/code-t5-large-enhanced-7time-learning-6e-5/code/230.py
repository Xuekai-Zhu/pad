def solution():
    
    # Define the number of tomatoes Steve eats per day
    daily_eats = 6

    # Calculate the number of tomatoes Steve needs per week
    weekly_tomatoes = daily_eats * 7

    # Calculate the number of vines Steve needs
    vines_needed = weekly_tomatoes // 3

    # Display the number of vines Steve needs
    result = vines_needed
    return result

print(solution())