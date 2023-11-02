def solution():
    """Alan likes to support music creators, so instead of downloading songs from the internet, he visits a record store once in a while. He decided now to buy 2 CDs by "The Dark", 1 CD by the creator "AVN", and 5 CDs that are mixes of songs from the 90s. The price of the "AVN" CD is $12 and it is half the price of one CD by "The Dark". The 5 CDs of 90s music cost is 40% of all the cost of all other CDs Alan is going to buy. How much will Alan have to pay for all the products?"""
    # Define the prices of the CDs
    avn_price = 12
    dark_price = None

    # Calculate the price of one CD by "The Dark"
    dark_price = 2 * avn_price

    # Calculate the price of all CDs except for the 90s mixes
    non_90s_price = (2 * dark_price) + avn_price

    # Calculate the cost of the 90s mixes
    ninety_price = non_90s_price * 0.4 / 5

    # Calculate the total cost
    total_cost = non_90s_price + (5 * ninety_price)

    # return the result
    result = total_cost
    return result

print(solution())