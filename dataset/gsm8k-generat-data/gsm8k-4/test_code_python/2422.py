def solution():
    """Hershel has 10 betta fish and 15 goldfish in a bowl. His friend Bexley brings him 2/5 times as many betta fish and 1/3 times as many goldfish. If Hershel gifts his sister 1/2 of the fish, calculate the total number of fish he has remaining in the bowl."""
    # Define the initial number of betta fish and goldfish
    initial_betta = 10
    initial_goldfish = 15

    # Calculate the number of betta fish and goldfish Bexley brings
    bexley_betta = 2/5 * initial_betta
    bexley_goldfish = 1/3 * initial_goldfish

    # Calculate the total number of fish
    total_betta = initial_betta + bexley_betta
    total_goldfish = initial_goldfish + bexley_goldfish
    total_fish = total_betta + total_goldfish

    # Calculate the number of fish Hershel gifts to his sister
    gifted_fish = total_fish / 2

    # Calculate the number of fish remaining in the bowl
    remaining_fish = total_fish - gifted_fish

    result = remaining_fish
    return result

print(solution())