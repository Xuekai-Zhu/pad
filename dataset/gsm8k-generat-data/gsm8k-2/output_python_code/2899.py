def solution():
    """James won a money prize at a charity raffle. He donated half of his winnings back to the charity, then spent $2 on a hot dog to celebrate his win. He had $55 left over. How many dollars did he win?"""
    remaining_money_after_hotdog = 55
    hotdog_price = 2
    remaining_money_before_donation = remaining_money_after_hotdog + hotdog_price
    donated_money = remaining_money_before_donation / 2
    total_money_won = remaining_money_before_donation + donated_money
    result = total_money_won
    return result

print(solution())