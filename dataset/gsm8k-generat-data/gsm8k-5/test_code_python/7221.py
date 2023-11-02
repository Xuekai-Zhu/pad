def solution():
    # Calculate total number of muffins needed
    total_muffins_needed = 120 / 2  # $120 needed divided by $2 per muffin

    # Calculate number of packs of muffins needed
    packs_needed = total_muffins_needed / 4  # Each pack contains 4 muffins

    # Calculate number of cases of muffins needed
    cases_needed = packs_needed / 3  # Each case contains 3 packs of muffins

    result = cases_needed
    return result

print(solution())