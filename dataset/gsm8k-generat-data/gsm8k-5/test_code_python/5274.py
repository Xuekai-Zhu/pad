def solution():
    mpg = 50  # Tom's car gets 50 miles to the gallon
    miles_per_day = 75  # Tom drives 75 miles per day
    days = 10  # Tom wants to know how much he will spend on gas in 10 days
    gas_price = 3  # Gas costs $3 per gallon

    # Calculate the total amount of gas consumed in 10 days
    gas_consumed = (miles_per_day * days) / mpg

    # Calculate the total cost of gas in 10 days
    total_cost = gas_consumed * gas_price
    result = total_cost
    return result

print(solution())