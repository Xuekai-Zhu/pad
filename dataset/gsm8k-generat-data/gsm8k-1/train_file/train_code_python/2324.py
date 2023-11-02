def solution():
    """George was selling some of his old toys on the internet. He managed to sell 3 little cars and a set of Legos. In total, he earned $45. How much did the Legos set cost, if one little car was sold for $5?"""
    total_earned = 45
    cars_sold = 3
    car_price = 5
    cars_total = cars_sold * car_price
    legos_price = total_earned - cars_total
    result = legos_price
    return result

print(solution())