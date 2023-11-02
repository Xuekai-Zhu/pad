def solution():
    """There are 10 cars parked in a mall’s parking lot, each with the same number of customers inside. Each customer only makes 1 purchase. If the sports store makes 20 sales and the music store makes 30 sales, how many customers are in each of the cars?"""
    total_customers = 20 + 30
    customers_per_car = total_customers / 10
    result = customers_per_car
    return result

print(solution())