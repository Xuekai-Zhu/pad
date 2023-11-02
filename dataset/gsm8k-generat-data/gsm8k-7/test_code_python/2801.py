def solution():
    num_chimp_legs = 4  # chimps have 4 legs
    num_lion_legs = 4  # lions have 4 legs
    num_lizard_legs = 4  # lizards have 4 legs
    num_tarantula_legs = 8  # tarantulas have 8 legs
    current_leg_count = 12*num_chimp_legs + 8*num_lion_legs + 5*num_lizard_legs 
    # calculate the current leg count of animals already seen
    remaining_legs = 1100 - current_leg_count  # calculate the remaining number of legs needed
    num_tarantulas_needed = remaining_legs / num_tarantula_legs  # calculate the number of tarantulas needed
    result = num_tarantulas_needed
    return result

print(solution())