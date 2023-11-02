def solution():
    # Calculate the amount earned from selling the baseball cards
    cards_earnings = 25

    # Calculate the amount earned from selling the baseball bat
    bat_earnings = 10

    # Calculate the discounted price of the baseball glove and the amount earned from selling it
    discounted_glove_price = 0.8 * 30
    glove_earnings = discounted_glove_price

    # Calculate the amount earned from selling the cleats
    cleats_earnings = 2 * 10

    # Calculate the total amount earned
    total_earnings = cards_earnings + bat_earnings + glove_earnings + cleats_earnings
    result = total_earnings
    return result

print(solution())