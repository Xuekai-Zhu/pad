def solution():
    """Jasper will serve charcuterie at his dinner party. He buys 2 pounds of cheddar cheese for $10, a pound of cream cheese that cost half the price of the cheddar cheese, and a pack of cold cuts that cost twice the price of the cheddar cheese. How much does he spend on the ingredients?"""
    cheddar_price = 5
    cream_cheese_price = cheddar_price / 2
    cold_cuts_price = cheddar_price * 2
    total_price = 2*cheddar_price + cream_cheese_price + cold_cuts_price
    result = total_price
    return result

print(solution())