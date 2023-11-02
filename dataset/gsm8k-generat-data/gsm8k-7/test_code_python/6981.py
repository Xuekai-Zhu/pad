def solution():
    initial_candy = 100
    daughter_eats = 8
    remaining_candy = initial_candy - daughter_eats
    num_bowls = 4
    taken_candy = 3*num_bowls
    remaining_candy = remaining_candy - taken_candy
    candy_per_bowl = remaining_candy/num_bowls
    result = candy_per_bowl
    return result

print(solution())