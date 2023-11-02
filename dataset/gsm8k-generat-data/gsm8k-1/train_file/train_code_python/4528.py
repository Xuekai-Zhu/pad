def solution():
    """Three builders build a single floor of a house in 30 days. If each builder is paid $100 for a single day’s work, how much would it cost to hire 6 builders to build 5 houses with 6 floors each?"""
    num_builders_per_floor = 3
    days_per_floor = 30
    cost_per_builder_per_day = 100
    num_builders_needed = 6
    num_houses = 5
    num_floors_per_house = 6

    total_floors = num_houses * num_floors_per_house
    total_days = total_floors * days_per_floor
    total_builders_needed = num_builders_per_floor * total_floors * num_builders_needed
    total_cost = total_builders_needed * cost_per_builder_per_day * total_days

    result = total_cost
    return result

print(solution())