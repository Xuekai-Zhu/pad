def solution():
    """The electricity price in Coco's town is $0.10 per kW. Coco's new oven has a consumption rate of 2.4 kWh (kilowatt-hours). How much will Coco pay for using his oven only if he used it for a total of 25 hours last month?"""
    # Define the cost per kilowatt-hour of electricity
    ELECTRICITY_PRICE = 0.1

    # Define the consumption rate of Coco's oven
    CONSUMPTION_RATE = 2.4

    # Define the number of hours Coco used his oven last month
    HOURS_USED = 25

    # Calculate the total electricity consumption
    total_consumption = CONSUMPTION_RATE * HOURS_USED

    # Calculate the total cost of using the oven
    total_cost = total_consumption * ELECTRICITY_PRICE

    # Display the total cost
    result = total_cost
    return result

print(solution())