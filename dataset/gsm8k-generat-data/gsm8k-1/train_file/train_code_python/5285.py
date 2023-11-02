def solution():
    """A florist offers for sale 75 narcissus flowers and 90 chrysanthemums. Using all the flowers, how many bouquets containing 5 flowers each can he make?"""
    total_flowers = 75 + 90
    flowers_per_bouquet = 5
    bouquets = total_flowers // flowers_per_bouquet
    result = bouquets
    return result

print(solution())