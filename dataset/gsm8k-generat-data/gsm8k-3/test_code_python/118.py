def solution():
    """Jeanette is practicing her juggling. Each week she can juggle 2 more objects than the week before. If she starts out juggling 3 objects and practices for 5 weeks, how many objects can she juggle?"""
    # Define the initial number of objects Jeanette can juggle
    objects = 3

    # Update the number of objects Jeanette can juggle each week and total the number of objects she can juggle after 5 weeks
    for i in range(5):
        objects += 2

    # Return the result
    result = objects
    return result

print(solution())