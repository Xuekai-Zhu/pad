def solution():
    """Bill is trying to decide whether to make blueberry muffins or raspberry muffins. Blueberries cost $5.00 per 6 ounce carton and raspberries cost $3.00 per 8 ounce carton. If Bill is going to make 4 batches of muffins, and each batch takes 12 ounces of fruit, how much money would he save by using raspberries instead of blueberries?"""
    # Define the prices and quantities of blueberries and raspberries
    blueberry_price = 5.00
    blueberry_quantity = 6  # ounces per carton
    raspberry_price = 3.00
    raspberry_quantity = 8  # ounces per carton

    # Define the number of batches and the required fruit quantity per batch
    num_batches = 4
    fruit_quantity_per_batch = 12  # ounces

    # Calculate the total cost of using blueberries
    blueberry_cost = (blueberry_price / blueberry_quantity) * fruit_quantity_per_batch * num_batches

    # Calculate the total cost of using raspberries
    raspberry_cost = (raspberry_price / raspberry_quantity) * fruit_quantity_per_batch * num_batches

    # Calculate the difference in cost between the two options
    cost_difference = blueberry_cost - raspberry_cost

    # Return the cost difference as a positive value
    result = abs(cost_difference)
    return result

print(solution())