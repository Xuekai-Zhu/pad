def solution():
    """Zach was a waiter in a fancy restaurant. His last table for the night was a party for 4 people. The mom ordered lobster for $25.50, the dad ordered steak for $35.00 their twin boys both ordered a cheeseburger and fries for $13.50 each. They started their meal with an appetizer that cost 8.50. Everyone also ordered a dessert that cost $6.00 each. They wanted to give a 20% tip for Zach on the bill. What did the final bill total come to?"""
    num_people = 4
    lobster_price = 25.50
    steak_price = 35.00
    burger_price = 13.50
    appetizer_price = 8.50
    dessert_price = 6.00
    tip_percent = 20

    meal_subtotal = lobster_price + steak_price + (2 * burger_price) + appetizer_price + (4 * dessert_price)
    tip_amount = meal_subtotal * (tip_percent / 100)
    total_bill = meal_subtotal + tip_amount
    
    result = total_bill
    return result

print(solution())