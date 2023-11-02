def solution():
    
    diamond_jewell_price = 2000
    gold_jewell_price = diamond_jewell_price * (4/5)
    silver_jewell_price = gold_jewell_price - 400
    total_price = diamond_jewell_price + gold_jewell_price + silver_jewell_price
    result = total_price
    return result

print(solution())