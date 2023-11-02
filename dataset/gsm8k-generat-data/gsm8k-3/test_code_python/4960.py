def solution():
    """Leticia, Scarlett, and Percy decide to eat at a Greek restaurant for lunch. The prices for their dishes cost $10, $13, and $17, respectively. If the trio gives the waiter a 10% tip, how much gratuity should the waiter receive in dollars?"""
    # Define the prices of each person's meal
    leticia_price = 10
    scarlett_price = 13
    percy_price = 17

    # Calculate the total cost of the meal
    total_cost = leticia_price + scarlett_price + percy_price

    # Calculate the gratuity amount
    gratuity = total_cost * 0.1

    # Display the gratuity amount
    result = gratuity
    return result

print(solution())