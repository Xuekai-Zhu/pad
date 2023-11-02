def solution():
    # Calculate the amount of potatoes Jason can eat in one minute
    potatoes_per_minute = 3/20  # Jason eats 3 potatoes in 20 minutes

    # Calculate the total amount of time in minutes it will take Jason to eat 27 potatoes
    total_minutes = 27 / potatoes_per_minute

    # Convert total_minutes to hours
    total_hours = total_minutes / 60

    result = total_hours
    return result

print(solution())