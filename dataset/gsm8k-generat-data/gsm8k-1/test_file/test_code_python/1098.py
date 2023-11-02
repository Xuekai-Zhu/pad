Sorry, I cannot provide a solution to the Samantha's last name problem as it requires additional information about the lengths of the last names of Bobbie and Jamie.

def solution():
    """Sheila charged $85.00 worth of merchandise on her credit card. She ended up returning one item that cost $15.00. After she returned the item, she bought a frying pan that was on sale for 20% off $20.00 and a set of towels that was 10% off $30.00. She put both of these purchases on her credit card. What is the new balance on her credit card?"""
    original_balance = 85.00
    returned_item_cost = 15.00
    frying_pan_cost = 20.00 * 0.80
    towels_cost = 30.00 * 0.90
    new_balance = original_balance - returned_item_cost + frying_pan_cost + towels_cost
    result = new_balance
    return result

print(solution())