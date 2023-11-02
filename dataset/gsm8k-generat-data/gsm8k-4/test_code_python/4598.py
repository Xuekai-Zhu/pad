def solution():
    """Juan bought T-shirts for his employees. He bought shirts for men and women. Women's t-shirts are $5 cheaper than men's t-shirts of the same color. His company has 2 sectors, one in white t-shirts and the other in black t-shirts. He paid $20 for white men's t-shirts and $18 for black men's t-shirts. The 2 sectors have the same number of men and women, with a total of 40 employees. How much did he spend total on buying t-shirts?"""
    # Define the price difference between men's and women's t-shirts
    tshirt_price_difference = 5

    # Define the prices of men's t-shirts
    white_mens_price = 20
    black_mens_price = 18

    # Define the number of employees in each sector
    sector_size = 20

    # Calculate the total cost of men's t-shirts in each sector
    white_mens_cost = white_mens_price * sector_size
    black_mens_cost = black_mens_price * sector_size

    # Calculate the total cost of women's t-shirts in each sector
    white_womens_cost = white_mens_cost - (tshirt_price_difference * sector_size)
    black_womens_cost = black_mens_cost - (tshirt_price_difference * sector_size)

    # Calculate the total cost of all t-shirts
    total_cost = (white_mens_cost + white_womens_cost + black_mens_cost + black_womens_cost)

    # Return the result
    result = total_cost
    return result

print(solution())