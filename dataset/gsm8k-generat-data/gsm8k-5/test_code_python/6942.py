def solution():
    kangaroo_legs = 2  # Each kangaroo has two legs
    goat_legs = 4  # Each goat has four legs
    num_kangaroos = 23  # Mark has 23 kangaroos
    num_goats = 3 * num_kangaroos  # He has three times as many goats as kangaroos

    # Calculate the total number of legs of all Mark's animals
    total_legs = (num_kangaroos * kangaroo_legs) + (num_goats * goat_legs)
    result = total_legs
    return result

print(solution())