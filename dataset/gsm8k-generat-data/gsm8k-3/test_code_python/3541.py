def solution():
    """There are 10 cars parked in a mall’s parking lot, each with the same number of customers inside. Each customer only makes 1 purchase. If the sports store makes 20 sales and the music store makes 30 sales, how many customers are in each of the cars?"""
    # Calculate the total number of customers
    total_customers = 20 + 30  # 20 sales from sports store, 30 sales from music store
    # Calculate the number of customers per car
    customers_per_car = total_customers / 10

    # Display the number of customers per car
    result = customers_per_car
    return result

print(solution())