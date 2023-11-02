def solution():
    """Aria has twice as many high school credits as Emily, who has twice the number of high school credits as Spencer.
    If Emily has 20 credits, what's twice the total number of high school credits the three have?"""
    emily_credits = 20
    spencer_credits = emily_credits / 2
    aria_credits = emily_credits * 2
    total_credits = emily_credits + spencer_credits + aria_credits
    result = 2 * total_credits
    return result

print(solution())