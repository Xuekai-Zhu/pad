def solution():
    """Jasper will serve charcuterie at his dinner party. He buys 2 pounds of cheddar cheese for $10, a pound of cream cheese that cost half the price of the cheddar cheese, and a pack of cold cuts that cost twice the price of the cheddar cheese. How much does he spend on the ingredients?"""
    # Define the cost of cheddar cheese and calculate the cost of cream cheese and cold cuts
    cheddar_cost = 10
    cream_cost = cheddar_cost / 2
    cold_cuts_cost = cheddar_cost * 2

    # Calculate the total cost of the ingredients
    total_cost = (2 * cheddar_cost) + cream_cost + cold_cuts_cost

    result = total_cost
    return result

print(solution())