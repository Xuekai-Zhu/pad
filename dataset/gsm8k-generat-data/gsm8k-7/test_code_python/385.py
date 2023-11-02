def solution():
    entrance_fee = 4
    price_per_pound = 20
    total_paid = 128

    # Calculate the total amount paid for strawberry picking, excluding the entrance fee
    total_harvest_cost = total_paid - entrance_fee * 3

    # Calculate the total amount of strawberries picked, in pounds
    total_strawberries = total_harvest_cost / price_per_pound
    result = total_strawberries
    return result

print(solution())