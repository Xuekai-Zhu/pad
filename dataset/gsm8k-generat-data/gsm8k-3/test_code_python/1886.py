def solution():
    """At the Sterling Auto Store, they have 500 cars for sale.  If they have 10 sales professionals, and each salesperson sells 10 cars per month, how many months will it take for them to sell all of the cars?"""
    # Define the total number of cars and sales professionals
    total_cars = 500
    salespeople = 10
    cars_sold_per_month = 10

    # Calculate the total number of cars sold per month
    total_cars_sold_per_month = salespeople * cars_sold_per_month

    # Calculate the number of months it will take to sell all the cars
    months_to_sell_all_cars = total_cars // total_cars_sold_per_month

    # Display the number of months
    result = months_to_sell_all_cars
    return result

print(solution())