def solution():
    # Set up equations based on given information
    # Let x be the size of Martha's bedroom
    # Then Jenny's bedroom is x + 60
    # Total square footage is x + (x + 60) = 2x + 60 = 300
    # Solve for x:
    x = (300 - 60) / 2
    result = x
    return result

print(solution())