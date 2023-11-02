def solution():
    # Find the total number of muffins Nora needs to sell
    total_price = 120  # target price for the school trip
    price_per_muffin = 2  # price per muffin
    muffins_needed = total_price / price_per_muffin  # total number of muffins needed

    # Find the number of cases of muffins Nora needs to sell
    muffins_per_pack = 4  # number of muffins per pack
    packs_per_case = 3  # number of packs per case
    muffins_per_case = muffins_per_pack * packs_per_case  # total number of muffins per case
    cases_needed = muffins_needed / muffins_per_case  # total number of cases needed
    result = int(cases_needed)  # round down to nearest integer
    return result

print(solution())