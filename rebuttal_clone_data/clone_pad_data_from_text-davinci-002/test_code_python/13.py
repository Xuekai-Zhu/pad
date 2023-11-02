def solution():
    """Jasper will serve charcuterie at his dinner party. He buys 2 pounds of cheddar cheese for $10, a pound of cream cheese that cost half the price of the cheddar cheese, and a pack of cold cuts that cost twice the price of the cheddar cheese. How much does he spend on the ingredients?"""
    cheddar_cheese_price = 10
    cheddar_cheese_weight = 2
    cream_cheese_price = cheddar_cheese_price / 2
    cream_cheese_weight = 1
    cold_cuts_price = cheddar_cheese_price * 2
    cold_cuts_weight = 1
    total_price = (cheddar_cheese_price * cheddar_cheese_weight) + (cream_cheese_price * cream_cheese_weight) + (cold_cuts_price * cold_cuts_weight)
    result = total_price
    
    return result

print(solution())