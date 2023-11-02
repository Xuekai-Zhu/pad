def solution():
    cost_of_barrettes = 3
    cost_of_comb = 1
    number_of_barrettes_bought_by_kristine = 1
    number_of_barrettes_bought_by_crystal = 3
    total_cost_of_kristines_purchase = cost_of_barrettes * number_of_barrettes_bought_by_kristine + cost_of_comb
    total_cost_of_crystals_purchase = cost_of_barrettes * number_of_barrettes_bought_by_crystal + cost_of_comb
    total_cost = total_cost_of_kristines_purchase + total_cost_of_crystals_purchase
    result = total_cost
    return result

print(solution())