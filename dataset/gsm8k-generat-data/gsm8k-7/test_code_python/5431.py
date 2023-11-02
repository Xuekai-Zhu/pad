def solution():
    total_gallons = 30
    # Let x be the number of gallons Adhira used
    x = (total_gallons + 5) / (4 + 1) # Using the given relationship between Adhira and Felicity's gas use
    # Calculate Felicity's gas use
    felicity_gallons = 4 * x - 5
    result = felicity_gallons
    return result

print(solution())