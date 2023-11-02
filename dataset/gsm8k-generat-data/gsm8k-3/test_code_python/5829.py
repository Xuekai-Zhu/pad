def solution():
    """Tas and his friends put up a t-shirt for sale. They ended up selling 200 t-shirts in 25 minutes. Half of the shirts were black and cost $30, while the other half were white and cost $25. How much money did they make per minute during the sale?"""
    # Define the number of black and white shirts sold
    black_shirts = 100
    white_shirts = 100

    # Define the cost of each color of shirt
    BLACK_COST = 30
    WHITE_COST = 25

    # Calculate the total money made from the black shirts
    black_money = black_shirts * BLACK_COST

    # Calculate the total money made from the white shirts
    white_money = white_shirts * WHITE_COST

    # Calculate the total money made during the sale
    total_money = black_money + white_money

    # Calculate the money made per minute
    money_per_minute = total_money / 25

    # Display the money made per minute
    result = money_per_minute
    return result

print(solution())