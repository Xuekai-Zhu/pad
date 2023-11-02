def solution():
    car_price = 14600
    savings = 14500
    num_trips = 40
    trip_fee = 1.5
    grocery_fee_percent = 0.05

    needed_savings = car_price - savings

    # Calculate the amount of money earned from delivering groceries
    grocery_fee = needed_savings - (num_trips * trip_fee)
    grocery_cost = grocery_fee / grocery_fee_percent

    result = grocery_cost
    return result

print(solution())