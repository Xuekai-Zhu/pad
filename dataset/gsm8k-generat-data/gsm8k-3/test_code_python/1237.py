def solution():
    """Laura is hosting a carwash. She will charge $5 for a car, $6 for a truck, and $7 for an SUV. They raised $100 in total. If they washed 5 SUVs and 5 trucks, how many cars did they wash?"""
    # Define the prices for each type of vehicle
    CAR_PRICE = 5
    TRUCK_PRICE = 6
    SUV_PRICE = 7

    # Define the number of each type of vehicle washed
    suvs_washed = 5
    trucks_washed = 5

    # Calculate the total amount raised from SUVs and trucks
    suvs_total = suvs_washed * SUV_PRICE
    trucks_total = trucks_washed * TRUCK_PRICE
    total_money = suvs_total + trucks_total

    # Calculate the number of cars washed
    cars_washed = (100 - total_money) / CAR_PRICE

    # Display the number of cars washed
    result = cars_washed
    return result

print(solution())