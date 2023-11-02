def solution():
    # Define the total calories Ellen should eat in a day
    total_calories = 2200
    
    # Define how many calories Ellen has eaten so far
    calories_eaten = 353 + 885 + 130
    
    # Calculate how many calories she has left for dinner
    calories_left = total_calories - calories_eaten
    
    result = calories_left
    return result

print(solution())