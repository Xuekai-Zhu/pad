def solution():
    total_cars = 500  # The store has 500 cars for sale
    num_salespeople = 10  # There are 10 sales professionals
    cars_sold_per_month = 10  # Each salesperson sells 10 cars per month

    # Calculate the total cars sold per month by all salespeople
    total_cars_sold_per_month = num_salespeople * cars_sold_per_month

    # Calculate the number of months it will take to sell all the cars
    months_to_sell_all_cars = total_cars / total_cars_sold_per_month
    result = months_to_sell_all_cars
    return result

print(solution())