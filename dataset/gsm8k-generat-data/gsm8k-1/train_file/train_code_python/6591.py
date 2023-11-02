def solution():
    """The square footage of the two bedrooms in the apartment that Jenny and Martha share totals 300 square feet. If Jenny's bedroom is 60 square feet larger than Martha's, how large, in square feet, is Martha's bedroom?"""
    total_square_footage = 300
    martha_square_footage = (total_square_footage - 60) / 2
    result = martha_square_footage
    return result

print(solution())