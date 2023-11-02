def solution():
    """Aria has twice as many high school credits as Emily, who has twice the number of high school credits as Spencer. If Emily has 20 credits, what's twice the total number of high school credits the three have?"""
    # Calculate the number of high school credits Spencer has
    spencer_credits = 20 / 2

    # Calculate the number of high school credits Emily has
    emily_credits = 20

    # Calculate the number of high school credits Aria has
    aria_credits = 20 * 2

    # Calculate the total number of high school credits the three have
    total_credits = spencer_credits + emily_credits + aria_credits

    # Calculate twice the total number of high school credits
    result = total_credits * 2
    return result

print(solution())