def solution():
    """Yesterday, the newly opened animal shelter received their first 60 animals. They got 20 more cats than dogs. How many cats did they take in?"""
    # Let x be the number of dogs
    # Then the number of cats is x + 20
    # And the total number of animals is x + (x + 20) = 2x + 20
    # We know that the total number of animals is 60, so 2x + 20 = 60
    # Solving for x, we get x = 20
    # Therefore, the number of cats is x + 20 = 40

    # Display the number of cats
    result = 40
    return result

print(solution())