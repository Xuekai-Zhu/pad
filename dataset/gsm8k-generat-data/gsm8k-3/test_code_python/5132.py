def solution():
    """Cid owns a mechanic shop, he charges $20 for an oil change, $30 for a repair, and $5 for a car wash. How much money did he earn if he changed the oil of 5 cars, repaired 10 cars, and washed 15 cars?"""
    # Define the prices for each service
    OIL_CHANGE_PRICE = 20
    REPAIR_PRICE = 30
    CAR_WASH_PRICE = 5

    # Define the number of cars for each service
    oil_changes = 5
    repairs = 10
    car_washes = 15

    # Calculate the total earned for oil changes
    oil_change_earnings = oil_changes * OIL_CHANGE_PRICE

    # Calculate the total earned for repairs
    repair_earnings = repairs * REPAIR_PRICE

    # Calculate the total earned for car washes
    car_wash_earnings = car_washes * CAR_WASH_PRICE

    # Calculate the total earnings
    total_earnings = oil_change_earnings + repair_earnings + car_wash_earnings

    # Display the total earnings
    result = total_earnings
    return result

print(solution())