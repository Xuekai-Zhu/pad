def solution():
    time_per_dog = 2.5 * 60  # Convert hours to minutes
    time_per_cat = 0.5 * 60  # Convert hours to minutes

    # Total time to groom 5 dogs and 3 cats
    total_time = (5 * time_per_dog) + (3 * time_per_cat)

    result = total_time
    return result

print(solution())