def solution():
    cost_of_soup = 2 * 6  # Mark buys 6 cans of soup for $2 each
    cost_of_bread = 5 * 2  # Mark buys 2 loaves of bread for $5 each
    cost_of_cereal = 3 * 2  # Mark buys 2 boxes of cereal for $3 each
    cost_of_milk = 4 * 2  # Mark buys 2 gallons of milk for $4 each

    total_cost = cost_of_soup + cost_of_bread + cost_of_cereal + cost_of_milk  # Calculate the total cost of the groceries
    
    # Calculate the number of $10 bills needed to pay
    num_of_10_bills_needed = total_cost // 10 + 1 if total_cost % 10 > 0 else total_cost // 10
    result = num_of_10_bills_needed
    return result

print(solution())