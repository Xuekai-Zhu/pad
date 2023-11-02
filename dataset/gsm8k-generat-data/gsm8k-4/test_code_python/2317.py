def solution():
    """Zach was a waiter in a fancy restaurant. His last table for the night was a party for 4 people. The mom ordered lobster for $25.50, the dad ordered steak for $35.00, their twin boys both ordered a cheeseburger and fries for $13.50 each. They started their meal with an appetizer that cost $8.50. Everyone also ordered a dessert that cost $6.00 each. They wanted to give a 20% tip for Zach on the bill. What did the final bill total come to?"""
    # Define the prices for each item
    lobster_price = 25.50
    steak_price = 35.00
    cheeseburger_price = 13.50
    appetizer_price = 8.50
    dessert_price = 6.00

    # Calculate the total cost of food
    food_cost = lobster_price + steak_price + (2 * cheeseburger_price) + appetizer_price + (4 * dessert_price)

    # Calculate the amount of the tip
    tip = 0.2 * food_cost

    # Calculate the total bill
    total_bill = food_cost + tip

    # Round the total bill to two decimal places
    result = round(total_bill, 2)
    return result

print(solution())