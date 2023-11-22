def solution():
    
    # Define the number of German Shepherds and Bulldogs kept
    german_shepherds = 3
    bulldogs = 2

    # Define the amount of dog food consumed per day by a German Shepherd and a Bulldog
    german_food_per_day = 5
    bulldog_food_per_day = 3

    # Calculate the total amount of dog food consumed per day
    total_food_per_day = (german_shepherds * german_food_per_day) + (bulldogs * bulldog_food_per_day)

    # Calculate the total amount of dog food consumed in a week
    total_food_per_week = total_food_per_day * 7

    # return the result
    result = total_food_per_week
    return result

print(solution())