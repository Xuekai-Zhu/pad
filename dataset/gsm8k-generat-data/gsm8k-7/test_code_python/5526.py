def solution():
    adoption_fee = 50
    vet_cost = 500
    monthly_food_cost = 25
    num_months = 12
    toy_cost = 200

    # Calculate the total cost of food for the first year
    food_cost_first_year = monthly_food_cost * num_months

    # Calculate the total cost of all shared expenses
    shared_cost = adoption_fee + vet_cost + food_cost_first_year

    # Calculate Jenny's total cost (including her own toys)
    jenny_cost = shared_cost + toy_cost / 2

    result = jenny_cost
    return result

print(solution())