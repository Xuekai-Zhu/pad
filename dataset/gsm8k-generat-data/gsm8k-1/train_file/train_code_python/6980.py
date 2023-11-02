def solution():
    """Boris has 100 pieces of Halloween candy. His daughter eats 8 pieces of candy. He separates the remaining pieces of candy into equal portions into 4 different bowls. Then he takes away 3 pieces of candy from each bowl to keep for himself. How many pieces of candy are in one bowl?"""
    initial_candy = 100
    candy_eaten = 8
    remaining_candy = initial_candy - candy_eaten
    candies_per_bowl = (remaining_candy // 4) - 3
    result = candies_per_bowl
    return result

print(solution())