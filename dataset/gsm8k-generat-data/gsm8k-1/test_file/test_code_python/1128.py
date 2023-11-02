def solution():
    """Valerie earns $5000 per month, 1/2 of what her brother earns. If their mother earns twice their combined salary, what's the total amount of money they all have together?"""
    valerie_earnings = 5000
    brother_earnings = valerie_earnings * 2
    combined_earnings = valerie_earnings + brother_earnings
    mother_earnings = 2 * combined_earnings
    total_earnings = valerie_earnings + brother_earnings + mother_earnings
    result = total_earnings
    return result

print(solution())