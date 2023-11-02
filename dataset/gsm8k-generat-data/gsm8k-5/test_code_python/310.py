def solution():
    # Calculate the wages for the warehouse workers
    warehouse_wages = 4 * 15 * 25 * 8  # 4 workers, $15/hour, 25 days a month, 8 hours a day

    # Calculate the wages for the managers
    manager_wages = 2 * 20 * 25 * 8  # 2 managers, $20/hour, 25 days a month, 8 hours a day

    # Calculate the total wages before taxes
    total_wages = warehouse_wages + manager_wages

    # Calculate the total FICA tax to be paid
    fica_tax = 0.1 * total_wages

    # Calculate the total amount Janet owes, including taxes
    total_owed = total_wages + fica_tax
    result = total_owed
    return result

print(solution())