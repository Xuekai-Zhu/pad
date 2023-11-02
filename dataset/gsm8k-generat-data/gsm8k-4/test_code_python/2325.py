def solution():
    """George was selling some of his old toys on the internet. He managed to sell 3 little cars and a set of Legos. In total, he earned $45. How much did the Legos set cost, if one little car was sold for $5?"""
    # Define the price of one little car
    car_price = 5

    # Calculate the earnings from selling the little cars
    car_earnings = car_price * 3

    # Calculate the earnings from selling the Legos set
    legos_earnings = 45 - car_earnings

    # Calculate the cost of the Legos set
    legos_cost = legos_earnings

    # return the result
    result = legos_cost
    return result

print(solution())