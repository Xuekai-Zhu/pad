def solution():
    # Define the initial amount of soda in each bottle
    soda_per_bottle = 1

    # Calculate the amount of soda Danny drank
    soda_drank = 0.9 * soda_per_bottle

    # Calculate the amount of soda Danny gave to his friends
    soda_given = 0.7 * 2 * soda_per_bottle

    # Calculate the total amount of soda remaining
    soda_remaining = 3 * soda_per_bottle - soda_drank - soda_given

    # Calculate the percentage of a bottle remaining
    percent_remaining = soda_remaining / soda_per_bottle * 100
    result = percent_remaining
    return result

print(solution())