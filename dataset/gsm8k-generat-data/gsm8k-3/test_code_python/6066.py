def solution():
    """Alan likes to support music creators, so instead of downloading songs from the internet, he visits a record store once in a while. He decided now to buy 2 CDs by "The Dark", 1 CD by the creator "AVN", and 5 CDs that are mixes of songs from the 90s. The price of the "AVN" CD is $12 and it is half the price of one CD by "The Dark". The 5 CDs of 90s music cost is 40% of all the cost of all other CDs Alan is going to buy. How much will Alan have to pay for all the products?"""
    # Define the price of the AVN CD and the ratio of its price to one CD by "The Dark"
    AVN_PRICE = 12
    PRICE_RATIO = 0.5

    # Define the number of CDs purchased for each type of music
    dark_cds = 2
    avn_cds = 1
    nineties_cds = 5

    # Calculate the price of one CD by "The Dark"
    dark_price = AVN_PRICE * 2

    # Calculate the total cost of all CDs except those from the 90s
    non_nineties_cost = (dark_cds * dark_price) + (avn_cds * AVN_PRICE)

    # Calculate the cost of the 90s CDs as 40% of the total cost of all other CDs
    nineties_cost = non_nineties_cost * 0.4

    # Calculate the total cost of all the CDs
    total_cost = non_nineties_cost + nineties_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())