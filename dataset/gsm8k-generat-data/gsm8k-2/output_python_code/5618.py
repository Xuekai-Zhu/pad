def solution():
    """Jack is counting out his register at the end of his shift in the shop. His till has 2 $100 bills, 1 $50 bill, 5 $20 bills, 3 $10 bills, 7 $5 bills, 27 $1 bills, and a certain amount of change in coins. If he is supposed to leave $300 in notes as well as all the coins in the till and turn the rest in to the main office, how much money will he be handing in?"""
    total_notes = 0
    total_notes += 2 * 100  # $100 bills
    total_notes += 1 * 50  # $50 bill
    total_notes += 5 * 20  # $20 bills
    total_notes += 3 * 10  # $10 bills
    total_notes += 7 * 5  # $5 bills
    total_notes += 27  # $1 bills
    coins = 0.0 # represent $0 in coins
    total_money = total_notes + coins
    money_to_turn_in = total_money - 300
    result = money_to_turn_in
    return result

print(solution())