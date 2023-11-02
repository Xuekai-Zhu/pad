def solution():
    onions_per_serving = 2  # Antoine's soup serves 6 people
    onions_per_pound = 2  # Antoine likes to double the amount of onions
    onions_cost = onions_per_serving * onions_per_pound  # The cost of onions is $2.00 per pound
    beef_stock_cost = 2  # The cost of 2 boxes of beef stock is $2.00 per box

    # Calculate the total cost of onions
    total_onions_cost = onions_per_serving * onions_cost

    # Calculate the total cost of beef stock
    total_beef_stock_cost = beef_stock_cost * 2  # Antoine needs 2 boxes of beef stock

    # Calculate the cost per serving
    cost_per_serving = total_onions_cost / 6  # Antoine's soup serves 6 people
    result = cost_per_serving
    return result

print(solution())