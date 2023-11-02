def solution():
    total_cars = 10  # There are 10 cars in the parking lot
    sports_sales = 20  # The sports store makes 20 sales
    music_sales = 30  # The music store makes 30 sales

    # Calculate the total number of customers in all the cars
    total_customers = sports_sales + music_sales

    # Calculate the average number of customers per car
    avg_customers_per_car = total_customers / total_cars
    result = avg_customers_per_car
    return result

print(solution())