def solution():
    """James has to refuel his plane. It used to cost $200 to refill the tank. He got an extra tank to double fuel capacity. Fuel prices also went up by 20%. How much does he pay now for fuel?"""
    
    original_cost = 200
    fuel_increase = 0.2
    new_cost = original_cost * (1 + fuel_increase)
    total_cost = new_cost * 2
    
    result = total_cost
    return result

print(solution())