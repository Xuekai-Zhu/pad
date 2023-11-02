def solution():
    """Fern buys one pair of high heels for $60 and five pairs of ballet slippers for 2/3rds of the price of the high heels. How much does she pay total?"""
    # Define the price of the high heels
    heels_price = 60

    # Calculate the price of one pair of ballet slippers
    slippers_price = heels_price * (2/3)

    # Calculate the total price of five pairs of ballet slippers
    total_slippers_price = slippers_price * 5

    # Calculate the total price Fern pays
    total_price = heels_price + total_slippers_price

    result = total_price
    return result

print(solution())