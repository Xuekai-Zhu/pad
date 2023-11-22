def solution():
    
    # Define the cost of the salad and yogurt
    SALAD_PRICE = 6
    YOGURT_PRICE = SALAD_PRICE / 2

    # Define the number of carrots eaten
    carrots_eaten = 3

    # Define the total cost of the goods
    total_cost = 11

    # Calculate the cost of the carrots eaten
    carrot_cost = (total_cost - SALAD_PRICE - YOGURT_PRICE) / carrots_eaten

    # Display the cost of one carrot
    result = carrot_cost
    return result

print(solution())