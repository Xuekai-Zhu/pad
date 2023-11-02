def solution():
    jogging_speed = 5  # Mira jogs 5 miles per hour
    jogging_time = 2  # Mira jogs for 2 hours every morning
    days = 5  # Mira wants to know how many miles she can jog in 5 days

    # Calculate the total distance Mira can jog in 5 days
    total_distance = jogging_speed * jogging_time * days
    result = total_distance
    return result

print(solution())