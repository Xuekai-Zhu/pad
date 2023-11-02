def solution():
    """Jasmine bought 4 pounds of coffee beans and 2 gallons of milk. A pound of coffee beans costs $2.50 and a gallon of milk costs $3.50. How much will Jasmine pay in all?"""
    # Define the cost of coffee beans and milk
    COFFEE_PRICE = 2.5
    MILK_PRICE = 3.5

    # Define the quantity of coffee beans and milk purchased
    coffee_qty = 4
    milk_qty = 2

    # Calculate the total cost of coffee beans and milk
    coffee_cost = coffee_qty * COFFEE_PRICE
    milk_cost = milk_qty * MILK_PRICE

    # Calculate the total cost of the purchase
    total_cost = coffee_cost + milk_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())