def solution():
    """James has to refuel his plane. It used to cost $200 to refill the tank. He got an extra tank to double fuel capacity. Fuel prices also went up by 20%. How much does he pay now for fuel?"""
    original_cost = 200
    new_capacity_cost = original_cost * 2
    price_increase = 0.2
    new_fuel_price = original_cost + (original_cost * price_increase)
    new_capacity_fuel_price = new_capacity_cost + (new_capacity_cost * price_increase)
    total_cost = new_fuel_price + new_capacity_fuel_price
    result = total_cost
    return result

print(solution())