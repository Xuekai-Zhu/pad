def solution():
    
    adoption_fee = 50
    vet_visits = 500
    food_cost = 25 * 12
    jenny_toys = 200
    total_cost = adoption_fee + vet_visits + food_cost + jenny_toys
    jenny_share = (total_cost - jenny_toys) / 2
    result = jenny_share + jenny_toys
    return result

print(solution())