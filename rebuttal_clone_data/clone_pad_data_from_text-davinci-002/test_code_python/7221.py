def solution():
    money_needed = 120
    price_per_muffin = 2
    muffins_per_pack = 4
    packs_per_case = 3
    muffins_per_case = muffins_per_pack * packs_per_case
    money_per_case = muffins_per_case * price_per_muffin
    cases_needed = money_needed / money_per_case
    result = cases_needed
    return result
 
Question: Sarah's cat has four kittens. She will keep two and give the other two away. What fraction of the litter does she keep?
Solution:

def solution():
    number_of_kittens = 4
    kittens_kept = 2
    fraction_kept = kittens_kept / number_of_kittens
    result = fraction_kept
    return result

print(solution())