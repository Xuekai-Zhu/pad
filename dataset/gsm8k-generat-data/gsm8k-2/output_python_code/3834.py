def solution():
    """Billy is breeding mice for an experiment. He starts with 8 mice, who each have 6 pups. When the pups grow up, all the mice have another 6 pups. Then each adult mouse eats 2 of their pups due to the stress of overcrowding. How many mice are left?"""
    starting_mice = 8
    starting_pups = starting_mice * 6
    next_gen_mice = starting_pups * 6
    total_mice = starting_mice + starting_pups + next_gen_mice
    eaten_mice = starting_mice * 2 + starting_pups * 2 + next_gen_mice * 2
    remaining_mice = total_mice - eaten_mice
    result = remaining_mice
    return result

print(solution())