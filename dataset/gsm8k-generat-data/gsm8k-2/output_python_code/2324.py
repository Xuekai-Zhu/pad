def solution():
    """George was selling some of his old toys on the internet. He managed to sell 3 little cars and a set of Legos. In total, he earned $45. How much did the Legos set cost, if one little car was sold for $5?"""
    little_car_price = 5
    total_earned = 45
    little_cars_sold = 3
    total_little_cars_price = little_cars_sold * little_car_price
    lego_set_price = total_earned - total_little_cars_price
    result = lego_set_price
    return result

print(solution())