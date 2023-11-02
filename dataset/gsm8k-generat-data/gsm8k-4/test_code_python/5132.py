def solution():
    """Cid owns a mechanic shop, he charges $20 for an oil change, $30 for a repair, and $5 for a car wash. How much money did he earn if he changed the oil of 5 cars, repaired 10 cars, and washed 15 cars?"""
    # Define the prices of oil change, repair, and car wash
    oil_change_price = 20
    repair_price = 30
    car_wash_price = 5

    # Define the number of cars serviced
    oil_change_cars = 5
    repair_cars = 10
    car_wash_cars = 15

    # Calculate the total earnings
    total_earnings = (oil_change_price * oil_change_cars) + (repair_price * repair_cars) + (car_wash_price * car_wash_cars)

    # return the result
    result = total_earnings
    return result

print(solution())