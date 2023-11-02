def solution():
    # Define the cost and quantity of each fruit
    lemon_cost = 2
    lemon_quantity = 6
    papaya_cost = 1
    papaya_quantity = 4
    mango_cost = 4
    mango_quantity = 2

    # Calculate the total cost before discount
    total_cost = lemon_cost * lemon_quantity + papaya_cost * papaya_quantity + mango_cost * mango_quantity

    # Calculate the number of fruit groups eligible for discount
    fruit_groups = (lemon_quantity + papaya_quantity + mango_quantity) // 4

    # Calculate the total discount
    discount = fruit_groups * 1

    # Calculate the final total cost after discount
    final_cost = total_cost - discount

    result = final_cost
    return result

print(solution())