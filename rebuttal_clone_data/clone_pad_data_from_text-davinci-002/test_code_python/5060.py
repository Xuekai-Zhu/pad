def solution():
    price_per_two_packs = 2.50
    price_per_pack = 1.30
    number_of_two_packs = 10
    total_price = price_per_two_packs * number_of_two_packs
    individual_price = price_per_pack * 2 * number_of_two_packs
    total_savings = individual_price - total_price
    result = total_savings
    return result

print(solution())