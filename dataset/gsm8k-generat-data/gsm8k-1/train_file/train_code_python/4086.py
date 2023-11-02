def solution():
    """Mitch has saved $20000 to finance his boating hobby. A new boat costs $1500 per foot in length. 
    If Mitch needs to keep $500 for a license and registration, and three times that amount for docking fees, 
    how many feet is the longest boat he can buy?"""
    
    total_budget = 20000
    license_fee = 500
    docking_fee = license_fee * 3
    available_budget = total_budget - (license_fee + docking_fee)
    cost_per_foot = 1500
    longest_boat_length = available_budget // cost_per_foot
    result = longest_boat_length
    return result

print(solution())