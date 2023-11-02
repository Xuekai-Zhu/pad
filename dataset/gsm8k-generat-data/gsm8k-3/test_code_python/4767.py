def solution():
    """Katerina purchases 3 pots and 4 pans at the home goods store. Each pot costs $20. The total cost of Katerina's items is $100. If each pan is the same price, what is the cost of 2 pans?"""
    # Define the cost of each pot
    POT_PRICE = 20

    # Define the number of pots purchased
    pot_count = 3

    # Define the total cost of Katerina's items
    total_cost = 100

    # Calculate the total cost of the pots
    pot_cost = pot_count * POT_PRICE

    # Calculate the cost of the pans
    pan_cost = total_cost - pot_cost

    # Calculate the cost of 2 pans
    two_pan_cost = pan_cost / 4 * 2

    # Display the cost of 2 pans
    result = two_pan_cost
    return result

print(solution())