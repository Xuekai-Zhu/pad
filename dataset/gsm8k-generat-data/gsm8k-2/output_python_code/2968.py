def solution():
    """Frank's laundry detergent is double concentrated and will wash 80 loads of laundry. His detergent is usually $25.00 a bottle but they're having a sale. If he buys 2 bottles, both bottles will drop to $20.00 a bottle. How much does he spend, in cents, per load of laundry, if he buys 2 bottles of detergent?"""
    regular_price = 25.00
    sale_price = 20.00
    bottles = 2
    loads_per_bottle = 80
    regular_price_per_load = regular_price / loads_per_bottle
    sale_price_per_load = (sale_price * bottles) / (loads_per_bottle * bottles)
    result = int(sale_price_per_load * 100)
    return result

print(solution())