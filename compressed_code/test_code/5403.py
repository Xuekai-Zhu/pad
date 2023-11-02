def solution():
    
    starting_candy = 100
    daughter_eats = 8
    remaining_candy = starting_candy - daughter_eats
    bowls = 4
    candy_per_bowl = (remaining_candy // bowls) - 3
    result = candy_per_bowl
    return result

print(solution())