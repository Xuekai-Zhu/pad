def solution():
    """Jeanette is practicing her juggling. Each week she can juggle 2 more objects than the week before. If she starts out juggling 3 objects and practices for 5 weeks, how many objects can she juggle?"""
    starting_objects = 3
    weeks_practiced = 5
    objects_per_week = 2
    total_objects = starting_objects
    for i in range(1, weeks_practiced):
        total_objects += (starting_objects + (i * objects_per_week))

    result = total_objects
    return result

print(solution())