def solution():
    """Jasper will serve charcuterie at his dinner party. He buys 2 pounds of cheddar cheese for $10, a pound of cream cheese that cost half the price of the cheddar cheese, and a pack of cold cuts that cost twice the price of the cheddar cheese. How much does he spend on the ingredients?"""
    cheddar_price_per_pound = 5
    cream_price_per_pound = cheddar_price_per_pound / 2
    cold_cut_price_per_pound = cheddar_price_per_pound * 2
    total_price = (2 * cheddar_price_per_pound) + cream_price_per_pound + cold_cut_price_per_pound
    result = total_price
    return result

print(solution())