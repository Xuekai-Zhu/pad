def solution():
    """Jeanette is practicing her juggling. Each week she can juggle 2 more objects than the week before. If she starts out juggling 3 objects and practices for 5 weeks, how many objects can she juggle?"""
    objects_juggled = 3
    weeks_practiced = 5
    additional_objects = 2
    total_objects = objects_juggled + (additional_objects * weeks_practiced)
    result = total_objects
    return result

print(solution())