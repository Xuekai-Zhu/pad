def solution():
    """The electricity price in Coco's town is $0.10 per kW. Coco's new oven has a consumption rate of 2.4 kWh (kilowatt-hours). How much will Coco pay for using his oven only if he used it for a total of 25 hours last month?"""
    electricity_price = 0.10
    consumption_rate = 2.4
    total_hours = 25
    total_consumed = consumption_rate * total_hours
    total_cost = total_consumed * electricity_price
    result = total_cost
    return result

print(solution())