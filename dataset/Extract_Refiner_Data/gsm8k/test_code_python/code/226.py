def solution():
    
    # Define the number of cars and the price per car
    NUM_CARS = 12
    CAR_PRICE = 20000

    # Calculate the total cost of the cars before tax and registration
    total_cost_before_tax = NUM_CARS * CAR_PRICE

    # Calculate the tax and registration cost for the cars
    tax_rate = 0.1
    registration_cost = 1000

    # Calculate the total cost of the cars with tax and registration
    total_cost_with_tax = total_cost_before_tax * (1 + tax_rate)

    # Calculate the total cost for registration
    total_cost_with_reg = total_cost_with_tax + registration_cost

    # Display the total cost
    result = total_cost_with_reg
    return result

print(solution())