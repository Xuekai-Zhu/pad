def solution():
    """Jason is tired of the neighborhood animals raiding his trash. He pepper-sprays some raccoons and 6 times as many squirrels. If he pepper-sprays 84 animals total, how many raccoons does he pepper-spray?"""
    # Let x be the number of raccoons pepper-sprayed
    # Then the number of squirrels pepper-sprayed is 6*x
    # The total number of animals pepper-sprayed is x + 6*x = 7*x
    # We know that 7*x = 84, so x = 12
    raccoons = 12

    # Return the number of raccoons pepper-sprayed
    result = raccoons
    return result

print(solution())