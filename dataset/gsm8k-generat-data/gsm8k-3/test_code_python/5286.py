def solution():
    """A florist offers for sale 75 narcissus flowers and 90 chrysanthemums. Using all the flowers, how many bouquets containing 5 flowers each can he make?"""
    # Define the total number of flowers
    total_flowers = 75 + 90

    # Calculate the number of bouquets that can be made
    num_bouquets = total_flowers // 5

    # Display the number of bouquets
    result = num_bouquets
    return result

print(solution())