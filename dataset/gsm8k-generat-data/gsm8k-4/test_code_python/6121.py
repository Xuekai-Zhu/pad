def solution():
    """Carrie wants to take a trip to New York. She can get a 20% discount on an $850 flight with Delta Airlines. She can also save 30% off an $1100 flight with United Airlines. How much money would she save by choosing the cheapest flight?"""
    # Define the prices of the Delta and United flights
    delta_price = 850
    united_price = 1100

    # Calculate the discounted prices of the Delta and United flights
    delta_discounted_price = delta_price * 0.8
    united_discounted_price = united_price * 0.7

    # Choose the flight with the lower discounted price
    if delta_discounted_price < united_discounted_price:
        cheaper_flight_price = delta_discounted_price
    else:
        cheaper_flight_price = united_discounted_price

    # Calculate the amount of money Carrie would save
    savings = abs(delta_price - cheaper_flight_price) if delta_discounted_price < united_discounted_price else abs(
        united_price - cheaper_flight_price)

    result = savings
    return result

print(solution())