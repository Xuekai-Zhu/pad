def solution():
    """Gretchen's local ice cream shop offers 100 different flavors. She was able to try a 1/4 of the flavors 2 years ago and double that amount last year. How many more flavors will she need to try this year to have tried all 100 flavors?"""
    # Define the total number of flavors and the number Gretchen has already tried
    total_flavors = 100
    flavors_tried = total_flavors / 4 + (total_flavors / 4) * 2

    # Calculate the number of flavors remaining to be tried
    flavors_remaining = total_flavors - flavors_tried

    # Return the result
    result = flavors_remaining
    return result

print(solution())