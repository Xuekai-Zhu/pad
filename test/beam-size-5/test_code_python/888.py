def solution():
    
    # Define the price of the salad and yogurt
    SALAD_PRICE = 6
    YOGURT_PRICE = SALAD_PRICE / 2

    # Define the number of carrots Ellen eats each day
    carrots_per_day = 2

    # Calculate the total cost of the goods
    total_cost = 11

    # Calculate the total cost of the carrots
    carrot_cost = total_cost - (salad_price + yogurt_price)

    # Display the total cost of one carrot
    result = carrot_cost
    return result

print(solution())