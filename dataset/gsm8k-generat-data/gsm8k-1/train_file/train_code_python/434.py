def solution():
    """Maria wants to buy a brand new bike. The retail price at the bike shop stands at $600. She saved $120 toward the purchase. As this was not enough, she asked her mother to give her the remaining amount. Her mother offered her $250 and told her that she needs to earn the rest working during the holidays. How much money must Maria earn to be able to buy the bike she wants?"""
    retail_price = 600
    saved_money = 120
    mother_contribution = 250
    remaining_money = retail_price - saved_money - mother_contribution
    result = remaining_money
    return result

print(solution())