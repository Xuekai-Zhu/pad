def solution():
    """Jeanette is practicing her juggling. Each week she can juggle 2 more objects than the week before. If she starts out juggling 3 objects and practices for 5 weeks, how many objects can she juggle?"""
    # Initialize the number of objects Jeanette can juggle
    objects_juggled = 3

    # Calculate the number of objects Jeanette can juggle after each week
    for i in range(1, 6):
        objects_juggled += 2

    # Return the final number of objects Jeanette can juggle
    result = objects_juggled
    return result

print(solution())