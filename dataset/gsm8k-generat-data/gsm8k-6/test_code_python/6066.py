def solution():
    # Calculate the price of one CD by "The Dark"
    price_The_Dark = 2 * 12 * 2  # Alan buys 2 CDs by "The Dark" and one of them costs twice as much as the "AVN" CD
    
    # Calculate the price of 5 CDs of 90s music
    price_90s_music = 0.4 * (price_The_Dark + 12)  # the price of 90s music CDs is 40% of the price of other CDs
    
    # Calculate the total price of all the products
    total_price = price_The_Dark + 12 + price_90s_music
    
    result = total_price
    return result

print(solution())