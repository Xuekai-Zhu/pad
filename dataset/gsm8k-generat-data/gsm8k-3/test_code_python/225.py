def solution():
    """Andy and Bob went to the canteen to buy snacks. They spent the same amount. Andy bought a can of soda at $1 and two hamburgers at $2 each.  Bob ordered two sandwiches for $3 and a can of fruit drink.  How much did Bob's fruit drink cost?"""
    # Define the prices of each item
    SODA_PRICE = 1
    HAMBURGER_PRICE = 2
    SANDWICH_PRICE = 1.5

    # Define the number of each item purchased by Andy and Bob
    andy_soda = 1
    andy_hamburgers = 2
    bob_sandwiches = 2
    bob_fruit_drink = 0

    # Calculate the total cost for Andy
    andy_total_cost = (andy_soda * SODA_PRICE) + (andy_hamburgers * HAMBURGER_PRICE)

    # Calculate the total cost for Bob
    bob_total_cost = (bob_sandwiches * SANDWICH_PRICE) + bob_fruit_drink

    # Calculate the cost of Bob's fruit drink
    bob_fruit_drink_cost = bob_total_cost - andy_total_cost

    # Display the cost of Bob's fruit drink
    result = bob_fruit_drink_cost
    return result

print(solution())