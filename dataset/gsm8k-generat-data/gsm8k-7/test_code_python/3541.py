def solution():
    total_cars = 10
    sports_sales = 20
    music_sales = 30

    # Calculate the total number of customers in all cars
    total_customers = sports_sales + music_sales

    # Calculate the average number of customers per car
    customers_per_car = total_customers / total_cars
    result = customers_per_car
    return result

print(solution())