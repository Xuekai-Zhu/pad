def solution():
    pie_cost_pfennigs = 2  # The cost of the meat pie is 2 pfennigs
    farthings_in_pfennig = 6  # There are 6 farthings in a pfennig
    total_farthings = 54  # Gerald has 54 farthings

    # Convert total farthings to pfennigs
    total_pfennigs = total_farthings / farthings_in_pfennig

    # Subtract pie cost from total pfennigs to get remaining pfennigs
    remaining_pfennigs = total_pfennigs - pie_cost_pfennigs
    result = remaining_pfennigs
    return result

print(solution())