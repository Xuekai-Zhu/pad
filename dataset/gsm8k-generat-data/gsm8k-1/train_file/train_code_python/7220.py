def solution():
    """Nora is selling muffins to raise $120 for an upcoming school trip. She has packaged the muffins in cases. Each case has three packs of muffins. Each pack has four muffins. If she prices each muffin at two dollars, how many cases of muffins must she sell to raise enough money for the trip?"""
    target_money = 120
    price_per_muffin = 2
    muffins_per_pack = 4
    packs_per_case = 3
    muffins_per_case = muffins_per_pack * packs_per_case
    money_per_case = muffins_per_case * price_per_muffin
    cases_to_sell = target_money / money_per_case
    result = int(cases_to_sell + 0.5) # rounding up to nearest integer
    return result

print(solution())