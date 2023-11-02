def solution():
    total_square_footage = 300  # The total square footage of the two bedrooms is 300

    # Let x be the size of Martha's bedroom
    # Then, Jenny's bedroom is x + 60
    # The total square footage is x + (x + 60) = 2x + 60

    # Solve for x
    x = (total_square_footage - 60) / 2

    result = x
    return result

print(solution())