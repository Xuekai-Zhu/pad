def solution():
    # Define the costs
    adoption_fee = 50
    vet_visits = 500
    food_cost = 25 * 12
    jenny_toys = 200

    # Calculate total costs
    total_costs = adoption_fee + vet_visits + food_cost + jenny_toys

    # Split costs in half since they agreed to split them with girlfriend
    jenny_spent = total_costs / 2

    result = jenny_spent
    return result

print(solution())