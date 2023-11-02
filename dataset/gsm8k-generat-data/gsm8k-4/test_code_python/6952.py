def solution():
    """Lauren wanted to make burgers and fries for dinner. She needed a few things from the grocery store and bought the following: 2 pounds of hamburger meat that was on sale for $3.50 a pound. 1 pack of hamburger buns for $1.50. A head of lettuce for $1.00 and a large 1.5-pound tomato that was priced at $2.00 per pound. She also needed a jar of pickles that cost $2.50 and she had a $1.00 off coupon for that item. How much change would Lauren get back if she paid with a $20 bill?"""
    
    # Define the prices for each item
    hamburger_meat_price = 3.5
    hamburger_buns_price = 1.5
    lettuce_price = 1.0
    tomato_price = 2.0
    pickles_price = 2.5
    pickles_discount = 1.0

    # Define the amount of each item purchased
    hamburger_meat_amount = 2
    hamburger_buns_amount = 1
    lettuce_amount = 1
    tomato_amount = 1.5
    pickles_amount = 1

    # Calculate the total cost of the groceries
    total_cost = (
        hamburger_meat_price * hamburger_meat_amount
        + hamburger_buns_price * hamburger_buns_amount
        + lettuce_price * lettuce_amount
        + tomato_price * tomato_amount
        + pickles_price * pickles_amount
        - pickles_discount
    )

    # Calculate the change after paying with a $20 bill
    change = 20 - total_cost

    result = round(change, 2)
    return result

print(solution())