def solution():
    starting_objects = 3  # Jeanette starts out juggling 3 objects
    objects_per_week = 2  # Jeanette can juggle 2 more objects per week
    total_objects = starting_objects  # Initialize total objects to starting objects
    for i in range(1, 6):  # Jeanette practices for 5 weeks
        total_objects += (starting_objects + objects_per_week * i)  # Add the number of objects Jeanette can juggle that week
    result = total_objects
    return result

print(solution())