def solution():
    original_price = 1200
    increase_percentage = 0.1
    decrease_percentage = 0.15

    # Calculate the price after the initial increase
    increased_price = original_price + (original_price * increase_percentage)

    # Calculate the price after the subsequent decrease
    final_price = increased_price - (increased_price * decrease_percentage)

    # Calculate the difference between the final price and the original price
    price_difference = original_price - final_price
    result = price_difference
    return result

print(solution())