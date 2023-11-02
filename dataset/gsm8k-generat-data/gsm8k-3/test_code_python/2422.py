def solution():
    """Hershel has 10 betta fish and 15 goldfish in a bowl. His friend Bexley brings him 2/5 times as many betta fish and 1/3 times as many goldfish. If Hershel gifts his sister 1/2 of the fish, calculate the total number of fish he has remaining in the bowl."""
    # Define the initial number of betta fish and goldfish
    INITIAL_BETTAS = 10
    INITIAL_GOLDFISH = 15

    # Calculate the number of betta fish and goldfish Bexley brings
    bexley_bettas = 2/5 * INITIAL_BETTAS
    bexley_goldfish = 1/3 * INITIAL_GOLDFISH

    # Calculate the total number of fish after Bexley's contribution
    total_bettas = INITIAL_BETTAS + bexley_bettas
    total_goldfish = INITIAL_GOLDFISH + bexley_goldfish
    total_fish = total_bettas + total_goldfish

    # Calculate the number of fish Hershel gifts his sister
    gifted_fish = 1/2 * total_fish

    # Calculate the number of fish remaining in the bowl
    remaining_fish = total_fish - gifted_fish

    # Display the number of fish remaining
    result = remaining_fish
    return result

print(solution())