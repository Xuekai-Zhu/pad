def solution():
    """The square footage of the two bedrooms in the apartment that Jenny and Martha share totals 300 square feet. If Jenny's bedroom is 60 square feet larger than Martha's, how large, in square feet, is Martha's bedroom?"""
    total_square_footage = 300
    difference = 60
    martha_sq_ft = (total_square_footage - difference) / 2
    result = martha_sq_ft
    return result

print(solution())