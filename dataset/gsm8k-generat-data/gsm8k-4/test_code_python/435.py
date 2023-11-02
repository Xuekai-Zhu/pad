def solution():
    """Maria wants to buy a brand new bike. The retail price at the bike shop stands at $600. She saved $120 toward the purchase. As this was not enough, she asked her mother to give her the remaining amount. Her mother offered her $250 and told her that she needs to earn the rest working during the holidays. How much money must Maria earn to be able to buy the bike she wants?"""
    
    # Define the retail price of the bike and the amount Maria has already saved
    retail_price = 600
    savings = 120

    # Calculate the amount Maria needs to earn
    amount_to_earn = retail_price - savings - 250

    result = amount_to_earn
    return result

print(solution())