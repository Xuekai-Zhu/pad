def solution():
    cost_of_burgers = 2 * 3.65  # Both Toby and his friend order a cheeseburger
    cost_of_milkshake = 2  # Toby orders a milkshake for $2
    cost_of_coke = 1  # Toby's friend orders a coke for $1
    cost_of_fries = 4  # They split a large fries that cost $4
    cost_of_cookies = 3 * 0.5  # Toby's friend orders three cookies for $0.5 each
    total_cost = cost_of_burgers + cost_of_milkshake + cost_of_coke + cost_of_fries + cost_of_cookies + 0.2  # Tax is $0.2
    amount_paid = 7.77  # Both Toby and his friend pay half of the total cost
    
    # Calculate the change Toby brings home
    change = 15 - amount_paid
    result = change
    return result

print(solution())