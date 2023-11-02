def solution():
    """Grant decided to sell his baseball gear since he was now playing football. He sold his baseball cards for $25. 
    He got $10 for his baseball bat and agreed to sell his $30 baseball glove at 20% off. 
    He also sold both pairs of his baseball cleats for $10 each. How much money did Grant make?"""

    baseball_cards_sale_price = 25
    baseball_bat_sale_price = 10
    baseball_glove_sale_price = 0.8 * 30
    baseball_cleats_sale_price = 2 * 10
    total_sale_price = baseball_cards_sale_price + baseball_bat_sale_price + baseball_glove_sale_price + baseball_cleats_sale_price
    result = total_sale_price
    return result

print(solution())