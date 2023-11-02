def solution():
    
    tshirt_cost = 20
    pants_cost = 80
    shoes_cost = 150

    discounted_tshirt_cost = 0.9 * tshirt_cost
    discounted_pants_cost = 0.9 * pants_cost
    discounted_shoes_cost = 0.9 * shoes_cost

    total_cost = (4 * discounted_tshirt_cost) + (3 * discounted_pants_cost) + (2 * discounted_shoes_cost)
    result = total_cost
    return result

print(solution())