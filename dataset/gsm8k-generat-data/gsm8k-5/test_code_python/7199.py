def solution():
    price_to_paint = 5  # Henry gets paid $5 to paint a bike
    price_to_sell = price_to_paint + 8  # Henry gets paid $8 more to sell a bike than to paint it
    num_bikes = 8  # Henry sells and paints 8 bikes

    # Calculate the total amount Henry gets paid for painting and selling 8 bikes
    total_price = (price_to_paint*num_bikes) + (price_to_sell*num_bikes)
    result = total_price
    return result

print(solution())