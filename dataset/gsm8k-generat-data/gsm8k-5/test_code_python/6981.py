def solution():
    starting_candy = 100  # Boris has 100 pieces of Halloween candy
    daughter_candy = 8  # Boris's daughter eats 8 pieces of candy
    remaining_candy = starting_candy - daughter_candy  # Boris has this many pieces of candy left
    bowls = 4  # Boris needs to divide the remaining candy among 4 bowls
    candy_per_bowl = (remaining_candy - 3 * bowls) / bowls  # Boris takes away 3 pieces of candy from each bowl

    result = candy_per_bowl
    return result

print(solution())