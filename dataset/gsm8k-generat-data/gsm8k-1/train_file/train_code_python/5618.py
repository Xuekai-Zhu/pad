def solution():
    """Jack is counting out his register at the end of his shift in the shop. His till has 2 $100 bills, 1 $50 bill, 5 $20 bills, 3 $10 bills, 7 $5 bills, 27 $1 bills, and a certain amount of change in coins.
    If he is supposed to leave $300 in notes as well as all the coins in the till and turn the rest in to the main office, how much money will he be handing in?"""
    
    # Calculating the total amount of money in notes
    money_in_notes = (2 * 100) + (1 * 50) + (5 * 20) + (3 * 10) + (7 * 5) + (27 * 1)
    
    # Subtracting the target amount to be left in notes from the total money in notes to get the amount to be turned in
    amount_to_turn_in = money_in_notes - 300
    
    result = amount_to_turn_in
    return result

print(solution())