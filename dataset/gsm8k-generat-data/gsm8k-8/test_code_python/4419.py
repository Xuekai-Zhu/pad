def solution():
    # Calculate the total cost of groceries
    total_cost = 6 * 2 + 2 * 5 + 2 * 3 + 2 * 4

    # Calculate the number of $10 bills needed to pay
    num_10_bills = total_cost // 10 + (total_cost % 10 > 0)

    result = num_10_bills
    return result

print(solution())