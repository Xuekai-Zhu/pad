def solution():
    """Juan bought T-shirts for his employees. He bought shirts for men and women. Women's t-shirts are $5 cheaper than men's t-shirts of the same color. His company has 2 sectors, one in white t-shirts and the other in black t-shirts. He paid $20 for white men's t-shirts and $18 for black men's t-shirts. The 2 sectors have the same number of men and women, with a total of 40 employees. How much did he spend total on buying t-shirts?"""
    # Define the prices of men's t-shirts
    WHITE_MEN_PRICE = 20
    BLACK_MEN_PRICE = 18

    # Define the price difference between men's and women's t-shirts
    WOMEN_PRICE_DIFF = 5

    # Calculate the price of women's t-shirts
    white_women_price = WHITE_MEN_PRICE - WOMEN_PRICE_DIFF
    black_women_price = BLACK_MEN_PRICE - WOMEN_PRICE_DIFF

    # Calculate the total number of t-shirts purchased
    total_shirts = 40

    # Calculate the number of men's t-shirts purchased
    men_shirts = total_shirts // 2

    # Calculate the number of women's t-shirts purchased
    women_shirts = total_shirts // 2

    # Calculate the total cost of the men's t-shirts
    men_cost = (WHITE_MEN_PRICE + BLACK_MEN_PRICE) * men_shirts

    # Calculate the total cost of the women's t-shirts
    women_cost = (white_women_price + black_women_price) * women_shirts

    # Calculate the total cost of all the t-shirts
    total_cost = men_cost + women_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())