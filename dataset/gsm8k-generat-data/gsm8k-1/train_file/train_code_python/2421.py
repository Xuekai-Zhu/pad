def solution():
    """Hershel has 10 betta fish and 15 goldfish in a bowl. His friend Bexley brings him 2/5 times as many betta fish and 1/3 times as many goldfish. If Hershel gifts his sister 1/2 of the fish, calculate the total number of fish he has remaining in the bowl."""
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