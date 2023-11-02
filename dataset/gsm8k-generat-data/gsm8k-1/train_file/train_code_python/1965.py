def solution():
    """Selina is selling some of her old clothes to a second-hand store. They will buy her pants for $5 each, her shorts for $3 each, and her shirts for $4 each. She sells 3 pairs of pants, 5 pairs of shorts, and some shirts. After she gets her money, she sees 2 shirts that she likes which cost $10 each and buys them. She leaves the store with $30. How many shirts did she sell to the store?"""
    pants_price = 5
    shorts_price = 3
    shirts_price = 4
    
    num_pants_sold = 3
    num_shorts_sold = 5
    
    total_pants_price = num_pants_sold * pants_price
    total_shorts_price = num_shorts_sold * shorts_price
    
    money_earned = total_pants_price + total_shorts_price + 2 * 10
    
    remaining_money = 30 - money_earned
    
    num_shirts_sold = remaining_money // shirts_price
    
    result = num_shirts_sold
    
    return result

print(solution())