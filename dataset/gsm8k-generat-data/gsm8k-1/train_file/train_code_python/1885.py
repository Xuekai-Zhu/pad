def solution():
    """At the Sterling Auto Store, they have 500 cars for sale. If they have 10 sales professionals, and each salesperson sells 10 cars per month, how many months will it take for them to sell all of the cars?"""
    total_cars = 500
    salespeople = 10
    cars_sold_per_month = 10
    total_cars_sold_per_month = salespeople * cars_sold_per_month
    months_to_sell_all_cars = total_cars / total_cars_sold_per_month
    result = months_to_sell_all_cars
    return result

print(solution())