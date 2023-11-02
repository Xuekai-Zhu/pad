def solution():
    """Gissela, Gordy, and Gary are truck drivers. Gissela has a truck large enough to haul 4,000 pounds of gravel. Gordy's truck can haul 800 pounds more than Gissela's truck. And when Gary brings his truck and joins Gissela and Gordy, the three trucks combined can haul a total of 11,600 pounds of gravel. How many pounds of gravel can Gary's truck carry?"""
    gissela_truck_capacity = 4000
    gordy_truck_capacity = gissela_truck_capacity + 800
    total_capacity = 11600
    gary_truck_capacity = total_capacity - (gissela_truck_capacity + gordy_truck_capacity)
    result = gary_truck_capacity
    return result

print(solution())