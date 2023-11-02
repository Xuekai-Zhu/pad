def solution():
    num_cars_for_sale = 500
    num_salespeople = 10
    cars_sold_per_salesperson_per_month = 10

    # Calculate the total number of cars sold per month by all salespeople
    total_cars_sold_per_month = num_salespeople * cars_sold_per_salesperson_per_month

    # Calculate the number of months it will take to sell all the cars
    months_to_sell_all_cars = num_cars_for_sale / total_cars_sold_per_month
    result = months_to_sell_all_cars
    return result

print(solution())