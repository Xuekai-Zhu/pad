def solution():
    budget = 200
    shirt_price = 30
    pants_price = 46
    coat_price = 38
    socks_price = 11
    belt_price = 18
    remaining_budget = 16

    # Calculate the total cost of all items except for shoes
    total_cost_without_shoes = shirt_price + pants_price + coat_price + socks_price + belt_price

    # Calculate the total amount spent on all items
    total_spent = budget - remaining_budget

    # Calculate the cost of the shoes by subtracting the total spent on all other items
    # from the total budget
    shoe_price = total_spent - total_cost_without_shoes
    result = shoe_price
    return result

print(solution())