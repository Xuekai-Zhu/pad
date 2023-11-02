def solution():
    # Calculate the total amount spent on the cat by Jenny
    adoption_fee = 50
    vet_visits = 500
    food_costs = 25 * 12  # monthly cost of food for 12 months
    toy_costs = 200
    total_cost = adoption_fee + vet_visits + food_costs + toy_costs
    jenny_spent = total_cost / 2  # she split the costs down the middle with her girlfriend
    result = jenny_spent
    return result

print(solution())