def solution():
    """A florist offers for sale 75 narcissus flowers and 90 chrysanthemums. Using all the flowers, how many bouquets containing 5 flowers each can he make?"""
    # Define the number of narcissus and chrysanthemums
    narcissus = 75
    chrysanthemums = 90

    # Calculate the total number of flowers
    total_flowers = narcissus + chrysanthemums

    # Calculate the number of bouquets that can be made
    bouquets = total_flowers // 5

    # Return the result
    result = bouquets
    return result

print(solution())