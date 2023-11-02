def solution():
    # Calculate the total number of muffins needed to raise $120
    muffin_total = 120 / 2

    # Calculate the number of packs needed, each case has 3 packs
    packs_needed = muffin_total / 4
    cases_needed = packs_needed / 3

    # Round up to the nearest whole number of cases
    cases_needed = math.ceil(cases_needed)
    result = cases_needed
    return result

print(solution())