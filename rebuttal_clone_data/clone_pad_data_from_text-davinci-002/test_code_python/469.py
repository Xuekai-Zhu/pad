def solution():
    hot_tub_size = 40
    champagne_size = 1
    champagne_cost = 50
    discount = 20
    final_cost = (champagne_cost * hot_tub_size * champagne_size) * (1 - (discount / 100))
    result = final_cost
    return result

print(solution())