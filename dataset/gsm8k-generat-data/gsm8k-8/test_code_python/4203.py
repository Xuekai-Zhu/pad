def solution():
    # Calculate the total monthly bills
    total_bills = 1250 + 150 + 400 + 300 + 200 + 200

    # Calculate the available funds for gas and maintenance
    available_funds = 3200 - total_bills - 350
    result = available_funds
    return result

print(solution())