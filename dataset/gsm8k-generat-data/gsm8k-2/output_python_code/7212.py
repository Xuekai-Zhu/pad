def solution():
    """Mike and John dined at the Taco Palace restaurant. They each ordered the Taco Grande Plate as their main meal, but Mike also ordered a side salad for $2, a plate of cheesy fries for $4, and a diet cola for $2. As a result, Mike's lunch bill was twice as large as John's bill. What was the combined total cost, in dollars, of Mike and John's lunch?"""
    taco_grande_price = 8
    mike_bill = taco_grande_price + 2 + 4 + 2
    john_bill = taco_grande_price
    total_cost = mike_bill + john_bill
    result = total_cost
    return result

print(solution())