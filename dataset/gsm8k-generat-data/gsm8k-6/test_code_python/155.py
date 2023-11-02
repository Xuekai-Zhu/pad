def solution():
    total_mangoes = 60  # kilograms
    sold_market = 20  # kilograms
    remaining_mangoes = (total_mangoes - sold_market) / 2  # kilograms
    remaining_mangoes *= 8  # each kilogram contains 8 mangoes
    result = remaining_mangoes
    return result

print(solution())