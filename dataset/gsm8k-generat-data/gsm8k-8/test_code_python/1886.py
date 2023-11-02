def solution():
    # Define the number of cars and salespeople
    total_cars = 500
    salespeople = 10
    cars_sold_per_month = 10

    # Calculate the total number of cars sold per month
    total_cars_sold_per_month = salespeople * cars_sold_per_month

    # Calculate the number of months it will take to sell all the cars
    months_to_sell_all_cars = total_cars / total_cars_sold_per_month

    result = months_to_sell_all_cars
    return result

print(solution())