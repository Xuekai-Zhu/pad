def solution():
    """Daria just got a new credit card so she could buy some furniture. Daria has $500 saved ready to pay for the furniture she buys, but the rest of the money will have to stay on her credit card statement until the next month, when she can pay it off with interest. She bought a couch for $750, a table for $100 and a lamp for $50. After she pays the initial $500, how much does she still owe before interest?"""
    initial_payment = 500
    couch_price = 750
    table_price = 100
    lamp_price = 50
    total_furniture_cost = couch_price + table_price + lamp_price
    remaining_balance = total_furniture_cost - initial_payment
    result = remaining_balance
    return result

print(solution())