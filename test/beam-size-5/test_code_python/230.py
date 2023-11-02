def solution():
    
    # Define the number of tomatoes Steve eats per day
    tomatoes_per_day = 6

    # Calculate the number of tomatoes Steve grows his own cherry tomatoes
    girlfriend_tomatoes = tomatoes_per_day * 2

    # Calculate the total number of tomatoes Steve eats in a week
    total_tomatoes_per_week = (tomatoes_per_day + girlfriend_tomatoes) * 7

    # Calculate the number of vines Steve needs to produce
    vines_needed = total_tomatoes_per_week / 3

    # Display the number of vines Steve needs to produce
    result = vines_needed
    return result

print(solution())