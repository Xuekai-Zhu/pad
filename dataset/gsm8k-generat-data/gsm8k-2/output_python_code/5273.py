def solution():
    """Tom's car gets 50 miles to the gallon. He drives 75 miles per day. If gas is $3 per gallon how much does he spend on gas in 10 days?"""
    miles_per_day = 75
    miles_per_gallon = 50
    gallons_per_day = miles_per_day / miles_per_gallon
    gas_price = 3
    total_cost = gallons_per_day * gas_price * 10
    result = total_cost
    return result

print(solution())