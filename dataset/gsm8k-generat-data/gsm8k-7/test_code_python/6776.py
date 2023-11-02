def solution():
    original_price =  # missing information
    sale_price = original_price * 0.8
    new_car_price = 30000
    additional_money_needed = 4000

    # Calculate the amount of money Liz received from selling her old car
    money_from_sale = sale_price

    # Calculate the total amount of money Liz has for her new car
    total_money = money_from_sale + additional_money_needed

    # Calculate the price difference between Liz's old car and her new car
    price_difference = original_price - new_car_price

    # Calculate how much cheaper Liz's new car is compared to her old car
    cheaper_by = price_difference - additional_money_needed
    result = cheaper_by
    return result

print(solution())