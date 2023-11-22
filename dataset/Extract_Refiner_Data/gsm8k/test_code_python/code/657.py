def solution():
    
    # Define the cost of the normal brand and the increase in cost for the expensive brand
    NORMAL_PRICE = 5
    PERCENT_INCREASE = 0.2

    # Define the cost of the expensive brand
    EXPECTED_PRICE = NORMAL_PRICE * (1 + PERCENT_INCREASE)

    # Define the cost of the donut
    DONUT_COST = 2

    # Calculate the total cost of the coffee
    total_cost = (1 * 7) * NORMAL_PRICE + DONUT_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())