def solution():
    """Gretchen's local ice cream shop offers 100 different flavors.  She was able to try a 1/4 of the flavors 2 years ago and double that amount last year.  How many more flavors will she need to try this year to have tried all 100 flavors?"""
    # Calculate the number of flavors Gretchen has already tried
    flavors_tried = 25 + 50  # 1/4 of 100 flavors, then double that amount

    # Calculate the number of flavors Gretchen still needs to try
    flavors_left = 100 - flavors_tried

    # Display the number of flavors Gretchen still needs to try
    result = flavors_left
    return result

print(solution())