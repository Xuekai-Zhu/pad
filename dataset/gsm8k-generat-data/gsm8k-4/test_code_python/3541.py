def solution():
    """There are 10 cars parked in a mall’s parking lot, each with the same number of customers inside. Each customer only makes 1 purchase. If the sports store makes 20 sales and the music store makes 30 sales, how many customers are in each of the cars?"""
    # Define the number of cars
    NUM_CARS = 10

    # Calculate the total number of customers from the sales in both stores
    total_customers = 20 + 30

    # Calculate the average number of customers per car
    customers_per_car = total_customers / NUM_CARS

    # Round the result to the nearest whole number
    result = round(customers_per_car)
    return result

print(solution())