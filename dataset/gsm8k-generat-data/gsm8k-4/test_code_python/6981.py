def solution():
    """Boris has 100 pieces of Halloween candy. His daughter eats 8 pieces of candy. He separates the remaining pieces of candy into equal portions into 4 different bowls. Then he takes away 3 pieces of candy from each bowl to keep for himself. How many pieces of candy are in one bowl?"""
    # Define the initial number of candies
    initial_candies = 100

    # Subtract the candies eaten by Boris's daughter
    remaining_candies = initial_candies - 8

    # Divide the remaining candies into 4 equal portions
    portions = 4
    candies_per_portion = remaining_candies / portions

    # Take away 3 candies from each portion
    candies_per_bowl = candies_per_portion - 3

    # return the result
    result = candies_per_bowl
    return result

print(solution())