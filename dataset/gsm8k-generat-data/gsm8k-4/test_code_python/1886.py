def solution():
    """At the Sterling Auto Store, they have 500 cars for sale. If they have 10 sales professionals, and each salesperson sells 10 cars per month, how many months will it take for them to sell all of the cars?"""
    # Define the total number of cars and the number of cars sold per month by each salesperson
    total_cars = 500
    cars_per_salesperson = 10

    # Calculate the total number of cars that can be sold in one month
    total_cars_sold_per_month = cars_per_salesperson * 10

    # Calculate the number of months it will take to sell all the cars
    months_to_sell_all_cars = total_cars / total_cars_sold_per_month

    # Round up to the nearest integer
    months_to_sell_all_cars = math.ceil(months_to_sell_all_cars)

    # Return the result
    result = months_to_sell_all_cars
    return result

print(solution())