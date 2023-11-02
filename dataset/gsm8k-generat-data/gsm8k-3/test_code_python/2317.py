def solution():
    """Zach was a waiter in a fancy restaurant.  His last table for the night was a party for 4 people.  The mom ordered lobster for $25.50, the dad ordered steak for $35.00 their twin boys both ordered a cheeseburger and fries for $13.50 each.  They started their meal with an appetizer that cost 8.50.  Everyone also ordered a dessert that cost $6.00 each.  They wanted to give a 20% tip for Zach on the bill.  What did the final bill total come to?"""
    # Define the prices of the items ordered
    LOBSTER_PRICE = 25.50
    STEAK_PRICE = 35.00
    CHEESEBURGER_PRICE = 13.50
    APPETIZER_PRICE = 8.50
    DESSERT_PRICE = 6.00

    # Calculate the cost of each item ordered
    lobster_cost = LOBSTER_PRICE
    steak_cost = STEAK_PRICE
    cheeseburger_cost = CHEESEBURGER_PRICE * 2
    appetizer_cost = APPETIZER_PRICE
    dessert_cost = DESSERT_PRICE * 4

    # Calculate the total cost of the meal
    total_cost = (lobster_cost + steak_cost + cheeseburger_cost
                  + appetizer_cost + dessert_cost)

    # Calculate the 20% tip for Zach
    tip = 0.2 * total_cost

    # Calculate the final bill total
    final_total = total_cost + tip

    # Display the final bill total
    result = final_total
    return result

print(solution())