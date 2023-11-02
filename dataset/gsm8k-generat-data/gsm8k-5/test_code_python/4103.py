def solution():
    budget = 60  # Abraham's budget is $60
    shower_gel_cost = 4  # Each shower gel costs $4
    num_shower_gels = 4  # Abraham buys 4 shower gels
    toothpaste_cost = 3  # The toothpaste costs $3
    remaining_budget = 30  # Abraham has $30 remaining in his budget

    # Calculate the total cost of the shower gels
    shower_gel_total_cost = shower_gel_cost * num_shower_gels

    # Calculate the total amount spent on toothpaste and shower gels
    total_spent = shower_gel_total_cost + toothpaste_cost

    # Calculate the amount spent on the laundry detergent
    laundry_detergent_cost = budget - total_spent - remaining_budget
    result = laundry_detergent_cost
    return result

print(solution())