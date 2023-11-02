def solution():
    """Carl caused a car accident that resulted in $40,000 worth of property damage and $70,000 worth of medical bills. If Carl's insurance company will pay 80% of the costs, leaving Carl to pay the remaining 20%, how much does Carl personally owe?"""
    property_damage = 40000
    medical_bills = 70000
    insurance_coverage = 0.8
    carl_share = 0.2
    total_cost = property_damage + medical_bills
    carl_owes = total_cost * carl_share
    result = carl_owes
    return result

print(solution())