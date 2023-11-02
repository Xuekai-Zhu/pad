def solution():
    """In ten years, I'll be twice my brother's age. The sum of our ages will then be 45 years old. How old am I now?"""
    # Let x be my current age and y be my brother's current age
    # In ten years, my age will be x + 10 and my brother's age will be y + 10
    # We know that in ten years, I'll be twice my brother's age, so:
    # x + 10 = 2(y + 10)
    # x + 10 = 2y + 20
    # x - 2y = 10

    # We also know that in ten years, the sum of our ages will be 45, so:
    # (x + 10) + (y + 10) = 45
    # x + y + 20 = 45
    # x + y = 25

    # We now have two equations with two variables, so we can solve for x
    # Start by rearranging the first equation to solve for y:
    # x - 2y = 10
    # -2y = -x + 10
    # y = (1/2)x - 5

    # Substitute this expression for y into the second equation:
    # x + y = 25
    # x + (1/2)x - 5 = 25
    # (3/2)x = 30
    # x = 20

    # Therefore, I am currently 20 years old
    result = 20
    return result

print(solution())