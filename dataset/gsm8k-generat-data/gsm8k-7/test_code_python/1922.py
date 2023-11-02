def solution():
    num_car_washes = 3
    car_wash_price = 10

    num_lawn_mows = 2
    lawn_mow_price = 13

    bike_price = 80

    # Calculate the total amount of money earned from car washes
    total_car_wash_money = num_car_washes * car_wash_price

    # Calculate the total amount of money earned from lawn mows
    total_lawn_mow_money = num_lawn_mows * lawn_mow_price

    # Calculate the total amount of money Stormi has earned
    total_money = total_car_wash_money + total_lawn_mow_money

    # Calculate the amount of money Stormi still needs to earn to afford the bike
    money_needed = bike_price - total_money
    result = money_needed
    return result

print(solution())