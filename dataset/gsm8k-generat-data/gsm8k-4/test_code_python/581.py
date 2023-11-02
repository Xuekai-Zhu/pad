def solution():
    """In ten years, I'll be twice my brother's age. The sum of our ages will then be 45 years old. How old am I now?"""
    # Let x be the current age of the speaker, and y be the current age of their brother
    # In 10 years, the speaker will be x + 10, and their brother will be y + 10
    # We are given that x + 10 = 2(y + 10), or equivalently, x - 2y = -10
    # We are also given that x + y + 20 = 45, or equivalently, x + y = 25

    # We can solve this system of equations to find x (the speaker's current age)
    # First, multiply the second equation by 2 and add it to the first equation to eliminate the x variable:
    # 2x - 4y = -20
    # x + y = 25
    # ------------
    # 3x - 3y = 5

    # Now, add 3y to both sides to isolate the x variable:
    # 3x = 5 + 3y

    # Finally, substitute the second equation into the above equation to solve for x:
    # 3x = 5 + 3y
    # 3x = 5 + 3(25-x)
    # 3x = 80 - 3x
    # 6x = 80
    # x = 13.33 (rounded to nearest whole number)

    result = round(x)
    return result

print(solution())