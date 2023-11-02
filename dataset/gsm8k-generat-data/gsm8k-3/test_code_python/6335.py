def solution():
    """Barry wants to make a huge salad using only cucumbers and tomatoes. He will use a total of 280 pieces of vegetables. If there are thrice as many tomatoes as cucumbers, how many cucumbers will be used in the salad?"""
    # Let's use variables to represent the number of cucumbers and tomatoes
    c = x  # Let x be the number of cucumbers
    t = 3 * x  # There are thrice as many tomatoes as cucumbers

    # The total number of vegetables is 280
    # We can write an equation to relate the number of cucumbers and tomatoes to the total number of vegetables
    c + t = 280

    # Substituting the expression for t in terms of x,
    c + 3x = 280

    # Simplifying the equation
    4x = 280
    x = 70

    # Therefore, Barry will use 70 cucumbers in the salad
    result = x
    return result

print(solution())