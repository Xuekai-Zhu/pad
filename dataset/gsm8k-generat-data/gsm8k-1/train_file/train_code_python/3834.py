def solution():
    """Billy is breeding mice for an experiment. He starts with 8 mice, who each have 6 pups. When the pups grow up, all the mice have another 6 pups. Then each adult mouse eats 2 of their pups due to the stress of overcrowding. How many mice are left?"""
    starting_mice = 8
    first_gen_pups = starting_mice * 6
    first_gen_mice = starting_mice + first_gen_pups
    second_gen_pups = first_gen_mice * 6
    second_gen_mice = first_gen_mice + second_gen_pups
    mice_lost = second_gen_mice // 2
    total_mice = second_gen_mice - mice_lost
    result = total_mice
    return result

print(solution())