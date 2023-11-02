def solution():
    """Laura is hosting a carwash. She will charge $5 for a car, $6 for a truck, and $7 for an SUV. They raised $100 in total. If they washed 5 SUVs and 5 trucks, how many cars did they wash?"""
    # Define the prices for each vehicle type
    CAR_PRICE = 5
    TRUCK_PRICE = 6
    SUV_PRICE = 7

    # Define the number of each vehicle washed
    SUV_COUNT = 5
    TRUCK_COUNT = 5

    # Calculate the total money raised
    total_money = (SUV_COUNT * SUV_PRICE) + (TRUCK_COUNT * TRUCK_PRICE) + ((100 - (SUV_COUNT + TRUCK_COUNT)*7 - TRUCK_COUNT*6)//5 * CAR_PRICE)

    # Calculate the number of cars washed
    car_count = (100 - (SUV_COUNT * SUV_PRICE) - (TRUCK_COUNT * TRUCK_PRICE)) // CAR_PRICE

    # return the result
    result = car_count
    return result

print(solution())