def solution():
    
    initial_betta_fish = 10
    initial_goldfish = 15
    bexley_betta_fish = (2/5) * initial_betta_fish
    bexley_goldfish = (1/3) * initial_goldfish
    total_fish = initial_betta_fish + initial_goldfish + bexley_betta_fish + bexley_goldfish
    gifted_fish = total_fish / 2
    remaining_fish = total_fish - gifted_fish
    result = remaining_fish
    return result

print(solution())