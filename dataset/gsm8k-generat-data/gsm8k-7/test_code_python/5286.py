def solution():
    num_narcissus = 75
    num_chrysanthemums = 90
    total_flowers = num_narcissus + num_chrysanthemums
    flowers_per_bouquet = 5
    num_bouquets = total_flowers // flowers_per_bouquet
    result = num_bouquets
    return result

print(solution())