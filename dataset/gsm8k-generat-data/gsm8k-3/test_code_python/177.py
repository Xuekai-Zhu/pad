def solution():
    """James decides to replace his car. He sold his $20,000 car for 80% of its value and then was able to haggle to buy a $30,000 sticker price car for 90% of its value. How much was he out of pocket?"""
    # Calculate the amount James received from selling his old car
    old_car_sold = 20000 * 0.8

    # Calculate the amount James paid for the new car
    new_car_bought = 30000 * 0.9

    # Calculate the difference between the two amounts, which is how much James is out of pocket
    out_of_pocket = new_car_bought - old_car_sold

    # return the result
    result = out_of_pocket
    return result

print(solution())