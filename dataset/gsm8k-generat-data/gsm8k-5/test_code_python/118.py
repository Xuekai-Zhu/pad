def solution():
    starting_objects = 3  # Jeanette starts by juggling 3 objects
    weeks_practiced = 5  # Jeanette practices for 5 weeks
    objects_per_week_increase = 2  # Each week, she can juggle 2 more objects than the week before

    # Calculate the total number of objects she can juggle after 5 weeks
    total_objects = 0
    for week in range(weeks_practiced):
        total_objects += starting_objects + week * objects_per_week_increase

    result = total_objects
    return result

print(solution())