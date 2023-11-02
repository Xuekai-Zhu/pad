def solution():
    """Gary does laundry twice a week. Each load of laundry uses 20 gallons of water, and a gallon of water costs $0.15. How much does Gary spend on water for laundry in a year?"""
    loads_per_week = 2
    gallons_per_load = 20
    cost_per_gallon = 0.15
    gallons_per_year = loads_per_week * gallons_per_load * 52
    cost_per_year = gallons_per_year * cost_per_gallon
    result = cost_per_year
    return result

print(solution())