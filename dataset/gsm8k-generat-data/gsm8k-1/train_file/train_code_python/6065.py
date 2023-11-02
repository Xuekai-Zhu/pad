def solution():
    """Alan likes to support music creators, so instead of downloading songs from the internet, he visits a record store once in a while. He decided now to buy 2 CDs by "The Dark", 1 CD by the creator "AVN", and 5 CDs that are mixes of songs from the 90s. The price of the "AVN" CD is $12 and it is half the price of one CD by "The Dark". The 5 CDs of 90s music cost is 40% of all the cost of all other CDs Alan is going to buy. How much will Alan have to pay for all the products?"""
    dark_cd_price = x
    avn_cd_price = 12
    dark_price = dark_cd_price * 2
    avn_price = avn_cd_price * 1
    ninety_cds_price = 0.4 * (dark_price + avn_price)
    total_price = dark_price + avn_price + ninety_cds_price
    result = total_price
    return result

# We cannot compute the solution as we do not have the value of "x" (price of one CD by "The Dark").

print(solution())