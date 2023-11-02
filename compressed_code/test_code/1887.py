def solution():
    
    initial_betta_fish = 10
    initial_goldfish = 15
    bexley_betta_fish = 2/5 * initial_betta_fish
    bexley_goldfish = 1/3 * initial_goldfish
    total_betta_fish = initial_betta_fish + bexley_betta_fish
    total_goldfish = initial_goldfish + bexley_goldfish
    total_fish = total_betta_fish + total_goldfish
    remaining_fish = 1/2 * total_fish
    result = total_fish - remaining_fish
    return result

print(solution())