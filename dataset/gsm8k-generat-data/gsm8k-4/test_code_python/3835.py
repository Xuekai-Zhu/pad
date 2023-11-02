def solution():
    """Billy is breeding mice for an experiment. He starts with 8 mice, who each have 6 pups. When the pups grow up, all the mice have another 6 pups. Then each adult mouse eats 2 of their pups due to the stress of overcrowding. How many mice are left?"""
    # Calculate the number of mice after the first generation of pups
    initial_mice = 8
    first_gen_pups = initial_mice * 6
    first_gen_mice = initial_mice + first_gen_pups

    # Calculate the number of mice after the second generation of pups
    second_gen_pups = first_gen_mice * 6
    second_gen_mice = first_gen_mice + second_gen_pups

    # Calculate the number of mice remaining after adults eat 2 of their pups
    remaining_mice = second_gen_mice - (second_gen_pups * 2)

    # Return the result
    result = remaining_mice
    return result

print(solution())