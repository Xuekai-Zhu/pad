def solution():
    
    # Define the cost of each item
    CHIPS_PRICE = 2
    CHICKEN_PRICE = 8
    SODA_PRICE = 1

    # Define the number of items purchased
    num_chips = 2
    num_chicken = 1
    num_sodas = 1

    # Calculate the total cost of the chips
    chips_cost = num_chips * CHIPS_PRICE

    # Calculate the total cost of the fried chicken
    chicken_cost = num_chicken * CHICKEN_PRICE

    # Calculate the total cost of the soda
    soda_cost = num_sodas * SODA_PRICE

    # Calculate the total cost of the apple pie
    pie_cost = 20 - chips_cost - chicken_cost - soda_cost

    # Display the cost of the apple pie
    result = pie_cost
    return result

print(solution())