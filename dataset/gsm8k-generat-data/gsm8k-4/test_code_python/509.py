def solution():
    """The electricity price in Coco's town is $0.10 per kW. Coco's new oven has a consumption rate of 2.4 kWh (kilowatt-hours). How much will Coco pay for using his oven only if he used it for a total of 25 hours last month?"""
    # Define the electricity price and oven consumption rate
    electricity_price = 0.10
    oven_consumption = 2.4

    # Define the number of hours the oven was used
    hours_used = 25

    # Calculate the total kilowatt-hours used
    total_kwh_used = oven_consumption * hours_used

    # Calculate the total cost of using the oven
    total_cost = total_kwh_used * electricity_price

    result = total_cost
    return result

print(solution())