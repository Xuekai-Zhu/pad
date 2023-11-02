def solution():
    adoption_fee = 50
    vet_visits = 500
    food_cost = 25 * 12  # Assuming 12 months in a year
    total_shared_cost = (adoption_fee + vet_visits + food_cost) / 2
    jenny_toy_cost = 200
    total_cost = total_shared_cost + jenny_toy_cost
    result = total_cost
    return result

print(solution())