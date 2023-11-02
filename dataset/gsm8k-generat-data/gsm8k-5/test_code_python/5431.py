def solution():
    total_gallons = 30  # Together, Felicity and Adhira used 30 gallons of gas
    adhira_gallons = (total_gallons + 5) / 4  # Felicity used 5 less gallons than 4 times Adhira's gallons
    felicity_gallons = total_gallons - adhira_gallons  # Find Felicity's gallons by subtracting Adhira's from the total

    result = felicity_gallons
    return result

print(solution())