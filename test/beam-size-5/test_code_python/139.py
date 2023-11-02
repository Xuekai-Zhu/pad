def solution():
    
    # Define the prices of each item
    milk_price = 2
    egg_price = 3
    light_bulbs_price = 3
    cup_price = 3
    roach_train_price = 4

    # Calculate the total cost before tax
    total_cost = milk_price + egg_price + light_bulbs_price + cup_price + roach_train_price

    # Calculate the tax
    tax = total_cost * 0.1

    # Calculate the total cost with tax
    total_cost_with_tax = total_cost + tax

    # Display the total cost with tax
    result = total_cost_with_tax
    return result

print(solution())