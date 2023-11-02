def solution():
    """Carla bought 2 bags of mini peanut butter cups on clearance.  Each bag was $6.00 but was 75% off. How much did she spend on 2 bags of candy?"""
    # Define the original price and discount rate
    original_price = 6.00
    discount_rate = 0.75

    # Calculate the sale price of one bag of candy
    sale_price = original_price * (1 - discount_rate)

    # Calculate the total cost of two bags of candy
    total_cost = sale_price * 2

    result = total_cost
    return result

print(solution())