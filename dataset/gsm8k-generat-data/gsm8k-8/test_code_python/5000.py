def solution():
    # Calculate the cost of the meat, crackers, vegetables, and cheese
    meat_cost = 5.00
    crackers_cost = 3.50
    vegetables_cost = 2.00 * 4
    cheese_cost = 3.50
    total_cost = meat_cost + crackers_cost + vegetables_cost + cheese_cost

    # Calculate the discount as 10% of the total cost
    discount = total_cost * 0.10

    # Calculate the final cost as the total cost minus the discount
    final_cost = total_cost - discount
    result = final_cost
    return result

print(solution())