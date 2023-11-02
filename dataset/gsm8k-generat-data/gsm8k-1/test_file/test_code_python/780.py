def solution():
    """Andy's car fuel efficiency is 10 MPG (miles per gallon). If the current price for regular gas is $3/gallon, how much money is Andy's car consuming per week if he only uses his car to go to work from Monday to Friday and the one-way distance between his home and office is 5 miles?"""
    mpg = 10
    price_per_gallon = 3
    distance_per_day = 5 * 2
    gallons_per_day = distance_per_day / mpg
    cost_per_day = gallons_per_day * price_per_gallon
    cost_per_week = cost_per_day * 5
    result = cost_per_week
    return result

print(solution())