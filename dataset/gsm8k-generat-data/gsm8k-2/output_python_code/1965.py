def solution():
    """Selina is selling some of her old clothes to a second-hand store. They will buy her pants for $5 each, her shorts for $3 each, and her shirts for $4 each. She sells 3 pairs of pants, 5 pairs of shorts, and some shirts. After she gets her money, she sees 2 shirts that she likes which cost $10 each and buys them. She leaves the store with $30. How many shirts did she sell to the store?"""
    pants_price = 5
    shorts_price = 3
    shirts_price = 4
    pants_sold = 3
    shorts_sold = 5
    total_sale = (pants_sold * pants_price) + (shorts_sold * shorts_price)
    remaining_money = 30 - total_sale
    shirts_bought = 2
    shirts_bought_price = 10
    remaining_money -= (shirts_bought * shirts_bought_price)
    shirts_sold = remaining_money / shirts_price
    result = shirts_sold
    return result

print(solution())