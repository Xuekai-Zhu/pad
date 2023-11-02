def solution():
    """Nora is selling muffins to raise $120 for an upcoming school trip. She has packaged the muffins in cases. Each case has three packs of muffins. Each pack has four muffins. If she prices each muffin at two dollars, how many cases of muffins must she sell to raise enough money for the trip?"""
    # Define the total amount needed for the school trip
    total_amount = 120

    # Calculate the total number of muffins needed to raise the required amount
    muffins_needed = total_amount / 2

    # Calculate the total number of packs needed
    packs_needed = muffins_needed / 4

    # Calculate the total number of cases needed
    cases_needed = packs_needed / 3

    # Round the number of cases up to the nearest integer
    cases_needed = int(cases_needed) + 1

    result = cases_needed
    return result

print(solution())