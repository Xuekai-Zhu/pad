def solution():
    """Grant decided to sell his baseball gear since he was now playing football. He sold his baseball cards for $25. He got $10 for his baseball bat and agreed to sell his $30 baseball glove at 20% off. He also sold both pair of his baseball cleats for $10 each. How much money did Grant make?"""
    baseball_cards = 25
    baseball_bat = 10
    baseball_glove = 30 * 0.8
    baseball_cleats = (10 * 2)
    total_money_made = baseball_cards + baseball_bat + baseball_glove + baseball_cleats
    result = total_money_made
    return result

print(solution())