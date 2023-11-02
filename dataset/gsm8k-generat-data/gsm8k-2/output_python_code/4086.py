def solution():
    """Mitch has saved $20000 to finance his boating hobby. A new boat costs $1500 per foot in length. If Mitch needs to keep $500 for a license and registration, and three times that amount for docking fees, how many feet is the longest boat he can buy?"""
    total_budget = 20000
    license_fee = 500
    docking_fee = 3 * license_fee
    available_budget = total_budget - license_fee - docking_fee
    boat_price_per_foot = 1500
    max_boat_length = available_budget // boat_price_per_foot
    result = max_boat_length
    return result

print(solution())