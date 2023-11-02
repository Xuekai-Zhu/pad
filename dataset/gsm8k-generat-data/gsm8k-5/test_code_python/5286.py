def solution():
    narcissus = 75  # The florist has 75 narcissus flowers for sale
    chrysanthemums = 90  # The florist has 90 chrysanthemums for sale
    total_flowers = narcissus + chrysanthemums  # The florist has a total of 165 flowers for sale
    flowers_per_bouquet = 5  # Each bouquet contains 5 flowers

    # Calculate the number of bouquets the florist can make
    bouquets = total_flowers // flowers_per_bouquet
    result = bouquets
    return result

print(solution())