def solution():
    """The local salon offers mani/pedis for $40.00.  They are running a Mother's day special and offering 25% off their regular rate.  Charlotte is treating herself, her daughter and 3 granddaughters to a spa day.  How much will Charlotte spend on 5 mani/pedis?"""
    # Define the regular rate and discount rate
    REGULAR_RATE = 40.00
    DISCOUNT_RATE = 0.25

    # Calculate the discounted rate
    discounted_rate = REGULAR_RATE - (REGULAR_RATE * DISCOUNT_RATE)

    # Calculate the total cost for 5 mani/pedis
    total_cost = discounted_rate * 5

    # Display the total cost
    result = total_cost
    return result

print(solution())