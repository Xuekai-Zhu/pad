def solution():
    """Felicity and Adhira took separate trips. Felicity used 5 less gallons of gas than four times the number of gallons that Adhira used for her trip. Together the girls used 30 gallons of gas. How many gallons did Felicity use?"""
    total_gallons = 30
    adhira_gallons = (total_gallons - 5) / 4
    felicity_gallons = adhira_gallons + 5
    result = felicity_gallons
    return result

print(solution())