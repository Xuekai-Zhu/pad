def solution():
    # Calculate the total amount of money spent and received by Mr. Ben
    total_spent = 600 + 1200  # cost of goods ordered and equipment maintenance
    total_received = 800  # amount received from debtor

    # Calculate the remaining balance for Mr. Ben
    remaining_balance = 2000 - total_spent + total_received
    result = remaining_balance
    return result

print(solution())