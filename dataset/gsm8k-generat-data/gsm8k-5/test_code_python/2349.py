def solution():
    burger_cost = 6
    soda_cost = burger_cost / 3
    jeremy_total = (2 * (burger_cost + soda_cost))
    paulo_total = burger_cost + soda_cost
    combined_total = jeremy_total + paulo_total
    result = combined_total
    return result

print(solution())