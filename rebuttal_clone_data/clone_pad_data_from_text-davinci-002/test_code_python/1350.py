def solution():
    caterpillars_per_jar = 10
    total_caterpillars = caterpillars_per_jar * 4
    butterflies = total_caterpillars * 0.6
    price_per_butterfly = 3
    total_revenue = butterflies * price_per_butterfly
    result = total_revenue
    return result

print(solution())