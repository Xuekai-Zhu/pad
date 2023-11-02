def solution():
    """Boris has 100 pieces of Halloween candy. His daughter eats 8 pieces of candy. He separates the remaining pieces of candy into equal portions into 4 different bowls. Then he takes away 3 pieces of candy from each bowl to keep for himself. How many pieces of candy are in one bowl?"""
    starting_candy = 100
    daughter_eats = 8
    remaining_candy = starting_candy - daughter_eats
    bowls = 4
    candy_per_bowl = (remaining_candy // bowls) - 3
    result = candy_per_bowl
    return result

print(solution())