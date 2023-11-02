def solution():
    """Frank's laundry detergent is double concentrated and will wash 80 loads of laundry. His detergent is usually $25.00 a bottle but they're having a sale. If he buys 2 bottles, both bottles will drop to $20.00 a bottle. How much does he spend, in cents, per load of laundry, if he buys 2 bottles of detergent?"""
    loads_per_bottle = 80
    regular_price = 2500
    sale_price = 2000
    price_per_load_regular = regular_price / loads_per_bottle
    price_per_load_sale = sale_price / (loads_per_bottle * 2)
    result = price_per_load_sale * 100
    return int(result)

print(solution())