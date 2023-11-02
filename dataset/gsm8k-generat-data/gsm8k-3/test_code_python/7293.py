def solution():
    """Brenda is a vet who needs to spay some cats and twice as many dogs. If she needs to spay 21 animals total today, how many cats does she need to spay?"""
    # Let x be the number of cats to spay
    # Then the number of dogs to spay is 2x
    # The total number of animals to spay is x + 2x = 3x
    # So we can set up the equation 3x = 21

    # Solve for x
    x = 21 / 3

    # Display the number of cats to spay
    result = x
    return result

print(solution())