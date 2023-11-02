def solution():
    """If Jason eats three potatoes in 20 minutes, how long, in hours, would it take for him to eat all 27 potatoes cooked by his wife?"""
    # Define the number of potatoes Jason can eat in a minute
    potatoes_per_minute = 3 / 20

    # Calculate the total number of minutes it will take Jason to eat all the potatoes
    total_minutes = 27 / potatoes_per_minute

    # Convert the minutes to hours
    total_hours = total_minutes / 60

    # return the result
    result = round(total_hours, 2)
    return result

print(solution())