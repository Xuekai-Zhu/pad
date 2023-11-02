def solution():
    """Mica went to the grocery store and bought 2 kilograms of pasta that costs $1.5; 1/4 kilogram of ground beef costs $8 for 1 kilogram; two jars of pasta sauce costs $2 per jar. Mica also wants to buy a $6 Quesadilla for snacks.  How much money should she have with her to buy all those?"""
    # Define the prices of each item
    PASTA_PRICE = 1.5
    BEEF_PRICE = 8/4
    SAUCE_PRICE = 2
    SNACK_PRICE = 6

    # Define the amount of each item purchased
    pasta_kg = 2
    beef_kg = 0.25
    sauce_jars = 2

    # Calculate the total cost of each item
    pasta_cost = PASTA_PRICE * pasta_kg
    beef_cost = BEEF_PRICE * beef_kg
    sauce_cost = SAUCE_PRICE * sauce_jars
    snack_cost = SNACK_PRICE

    # Calculate the total cost of the items
    total_cost = pasta_cost + beef_cost + sauce_cost + snack_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())