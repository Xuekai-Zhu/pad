def solution():
    starting_objects = 3
    weeks = 5
    objects_per_week_increase = 2

    # Calculate the total number of objects she can juggle after five weeks
    total_objects = starting_objects
    for i in range(weeks):
        total_objects += objects_per_week_increase
        objects_per_week_increase += 2

    result = total_objects
    return result

print(solution())