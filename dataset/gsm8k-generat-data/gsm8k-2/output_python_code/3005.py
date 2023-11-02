def solution():
    """Gretchen's local ice cream shop offers 100 different flavors. She was able to try a 1/4 of the flavors 2 years ago and double that amount last year. How many more flavors will she need to try this year to have tried all 100 flavors?"""
    total_flavors = 100
    tried_flavors = (total_flavors / 4) * 2  # she tried 1/4 of the flavors 2 years ago and doubled that amount last year
    remaining_flavors = total_flavors - tried_flavors
    result = remaining_flavors
    return result

print(solution())