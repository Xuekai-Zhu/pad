def solution():
    """Fred wants to order a variety pack of sliced meats for the upcoming game. He can order a 4 pack of fancy, sliced meat for $40.00 and add rush delivery for an additional 30%. With rush shipping added, how much will each type of sliced meat cost?"""
    # Define the price of the 4 pack of fancy, sliced meat and the rush delivery percentage
    pack_price = 40
    rush_delivery_percent = 0.3

    # Calculate the total price with rush delivery
    total_price = pack_price * (1 + rush_delivery_percent)

    # Calculate the price per type of sliced meat
    price_per_type = total_price / 4

    # return the result
    result = price_per_type
    return result

print(solution())