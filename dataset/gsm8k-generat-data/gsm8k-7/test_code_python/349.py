def solution():
    total_animals = 56

    # Let's assume the number of goats as 'x'
    num_goats = x

    # Number of cows is 4 more than goats
    num_cows = x + 4

    # Number of pigs is twice as many as cows
    num_pigs = 2 * num_cows

    # Total animals
    total_animals = num_goats + num_cows + num_pigs

    # Equation to solve for x
    x = (total_animals - 8) / 3

    result = int(x)
    return result

print(solution())