def solution():
    # Let x be the size of Martha's bedroom (in square feet)
    # Then, Jenny's bedroom is x + 60 square feet

    # The total square footage is 300, so we can write:
    x + (x+60) = 300

    # Simplifying and solving for x:
    2x + 60 = 300
    2x = 240
    x = 120

    # Therefore, Martha's bedroom is 120 square feet
    result = x
    return result

print(solution())