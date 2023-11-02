def solution():
    num_kangaroos = 23
    num_goats = 3 * num_kangaroos

    kangaroo_legs = 2
    goat_legs = 4

    # Calculate the total number of legs for kangaroos
    total_kangaroo_legs = num_kangaroos * kangaroo_legs

    # Calculate the total number of legs for goats
    total_goat_legs = num_goats * goat_legs

    # Calculate the total number of legs for all animals
    total_legs = total_kangaroo_legs + total_goat_legs
    result = total_legs
    return result

print(solution())