def solution():
    # Calculate the total cost of wigs for all acts in 3 plays
    total_wigs_cost = 2 * 5 * 5 * 3  # 2 wigs per act, 5 acts per play, 3 plays, each wig cost $5
    # Calculate the money earned by selling all wigs for 1 play
    sold_wigs_money = 4 * 2 * 5 * 5  # all wigs for 1 play sold for $4 per wig
    # Calculate the total money spent
    total_money_spent = total_wigs_cost - sold_wigs_money  # John dropped 1 play and sold all wigs for that play
    result = total_money_spent
    return result

print(solution())