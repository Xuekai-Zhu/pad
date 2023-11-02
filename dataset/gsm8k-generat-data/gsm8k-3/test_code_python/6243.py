def solution():
    """Jebb buys $50 worth of food at a restaurant with a service fee of 12%. After paying, he gives a $5 tip. How much money did he spend at the restaurant?"""
    # Define the cost of the food
    food_cost = 50

    # Define the service fee percentage
    service_fee_percent = 0.12

    # Calculate the service fee amount
    service_fee = food_cost * service_fee_percent

    # Calculate the total cost of the food and service fee
    total_cost = food_cost + service_fee

    # Add the tip to the total cost
    total_cost += 5

    # Display the total cost
    result = total_cost
    return result

print(solution())