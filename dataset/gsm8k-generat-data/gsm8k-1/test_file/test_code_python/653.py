def solution():
    """James buys a plane. The plane cost $150,000. He pays $5000 a month to rent a hanger to keep it in. He also spends twice as much as that on fuel per month. How much did it cost him to get and maintain the plane for the first year?"""
    plane_cost = 150000
    hangar_cost_per_month = 5000
    fuel_cost_per_month = hangar_cost_per_month * 2
    maintenance_cost_per_month = hangar_cost_per_month + fuel_cost_per_month
    total_maintenance_cost_per_year = maintenance_cost_per_month * 12
    total_cost = plane_cost + total_maintenance_cost_per_year
    result = total_cost
    return result

print(solution())