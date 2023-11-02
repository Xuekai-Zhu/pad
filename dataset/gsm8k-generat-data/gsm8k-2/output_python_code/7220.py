def solution():
    """Nora is selling muffins to raise $120 for an upcoming school trip. She has packaged the muffins in cases. Each case has three packs of muffins. Each pack has four muffins. If she prices each muffin at two dollars, how many cases of muffins must she sell to raise enough money for the trip?"""
    money_needed = 120
    muffin_price = 2
    muffins_per_pack = 4
    packs_per_case = 3
    muffins_per_case = packs_per_case * muffins_per_pack
    cases_needed = money_needed / (muffins_per_case * muffin_price)
    result = cases_needed
    return result

print(solution())