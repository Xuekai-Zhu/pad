def solution():
    """Nora is selling muffins to raise $120 for an upcoming school trip. She has packaged the muffins in cases. Each case has three packs of muffins. Each pack has four muffins. If she prices each muffin at two dollars, how many cases of muffins must she sell to raise enough money for the trip?"""
    # Define the number of muffins needed to raise $120
    muffins_needed = 120 / 2  # $2 per muffin

    # Calculate the number of packs of muffins needed
    packs_needed = muffins_needed / 4  # 4 muffins per pack

    # Calculate the number of cases of muffins needed
    cases_needed = packs_needed / 3  # 3 packs per case

    # Round up to the nearest whole number of cases
    cases_needed = math.ceil(cases_needed)

    # Display the number of cases of muffins needed
    result = cases_needed
    return result

print(solution())