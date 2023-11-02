def solution():
    """The square footage of the two bedrooms in the apartment that Jenny and Martha share totals 300 square feet. If Jenny's bedroom is 60 square feet larger than Martha's, how large, in square feet, is Martha's bedroom?"""
    # Define the total square footage of both bedrooms and the size difference between them
    total_square_footage = 300
    difference = 60

    # Calculate Martha's bedroom size using algebraic equation
    martha_square_footage = (total_square_footage - difference) / 2

    # Return the result
    result = martha_square_footage
    return result

print(solution())