def solution():
    sunscreen_per_month = 1
    sunscreen_cost = 30
    months_per_year = 12
    total_sunscreen = sunscreen_per_month * months_per_year
    discount = 30
    total_cost = sunscreen_cost * total_sunscreen
    final_cost = total_cost - ((discount / 100) * total_cost)
    result = final_cost
    return result

print(solution())