def solution():
    # Define the original prices and the new prices 
    backpack_original_price = 50
    backpack_new_price = backpack_original_price + 5
    binder_original_price = 20
    binder_new_price = binder_original_price - 2

    # Calculate the total cost of the backpack and the three binders
    total_cost_original = backpack_original_price + 3*binder_original_price
    total_cost_new = backpack_new_price + 3*binder_new_price

    # Return the difference in cost
    result = total_cost_new - total_cost_original
    return result

print(solution())