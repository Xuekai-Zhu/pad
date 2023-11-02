def solution():
    cost_in_pfennigs = 2
    farthings = 54
    farthings_per_pfennig = 6

    # Convert farthings to pfennigs
    total_in_pfennigs = farthings / farthings_per_pfennig

    # Calculate the amount left after buying the pie
    amount_left = total_in_pfennigs - cost_in_pfennigs

    result = amount_left
    return result

print(solution())