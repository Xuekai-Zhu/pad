def solution():
    """Jack is on the phone with a scammer who says the IRS will arrest Jack if he doesn't send them the codes from 6 $500 Best Buy gift cards and 9 $200 Walmart gift cards. After sending the codes for 1 Best Buy gift card and 2 Walmart gift cards, Jack wises up and hangs up. How many dollars' worth of gift cards can he still return?"""
    best_buy_cards = 6
    walmart_cards = 9
    best_buy_value = 500
    walmart_value = 200
    codes_sent = (1 * best_buy_value) + (2 * walmart_value)
    total_value = (best_buy_cards * best_buy_value) + (walmart_cards * walmart_value)
    remaining_value = total_value - codes_sent
    result = remaining_value
    
    return result

print(solution())