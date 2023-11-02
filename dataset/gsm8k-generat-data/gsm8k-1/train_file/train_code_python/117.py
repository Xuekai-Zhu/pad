def solution():
    """Jeanette is practicing her juggling. Each week she can juggle 2 more objects than the week before.
    If she starts out juggling 3 objects and practices for 5 weeks, how many objects can she juggle?"""
    starting_objects = 3
    weeks_practicing = 5
    objects_per_week = 2
    total_objects = starting_objects + (objects_per_week * (weeks_practicing - 1))
    result = total_objects
    return result

print(solution())