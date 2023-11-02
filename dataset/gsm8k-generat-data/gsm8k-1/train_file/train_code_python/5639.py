def solution():
    """Phantom's mom gave him $50 to buy printer-inks. At the store, he bought two black printer inks which cost $11 each, 
    three red printer inks which cost $15 each, and two yellow printer inks which cost $13 each. Phantom found out that his 
    money is not enough to buy all the printer inks. How much more money should he ask his mom to be able to buy the printer 
    inks?"""
    budget = 50
    black_ink_cost = 11
    red_ink_cost = 15
    yellow_ink_cost = 13
    black_inks_bought = 2
    red_inks_bought = 3
    yellow_inks_bought = 2
    total_cost = (black_ink_cost * black_inks_bought) + (red_ink_cost * red_inks_bought) + (yellow_ink_cost * yellow_inks_bought)
    more_money_needed = total_cost - budget
    result = more_money_needed
    
    return result

print(solution())