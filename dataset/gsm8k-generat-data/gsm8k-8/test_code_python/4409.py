def solution():
    # Define the number of cases and tins per case
    num_cases = 15
    tins_per_case = 24

    # Calculate the total number of tins before any were damaged
    total_tins = num_cases * tins_per_case

    # Calculate the number of tins that are damaged and need to be thrown away
    num_damaged_tins = 0.05 * total_tins

    # Calculate the number of tins left after the damaged ones are thrown away
    tins_left = total_tins - num_damaged_tins
    result = tins_left
    return result

print(solution())