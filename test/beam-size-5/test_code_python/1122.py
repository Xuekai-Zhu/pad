def solution():
    distance_per_day = 400  # Alfie flies 400 kilometers every day
    total_distance = 40000  # The circumference of the earth is 40,000 kilometers

    # Calculate the distance Alfie needs to fly around the earth
    distance_to_fly = 0.5 * total_distance

    # Calculate the number of days it will take Alfie to fly around the earth
    days_to_fly = distance_to_fly / distance_per_day
    result = days_to_fly
    return result

print(solution())