def solution():
    # Calculate the total cost of the kombucha
    total_cost = 15 * 12 * 3.00  # 15 bottles per month for 12 months, each bottle costs $3.00

    # Calculate the total amount of refund he will receive
    total_refund = 15 * 12 * 0.10  # 15 bottles per month for 12 months, $0.10 refund per bottle

    # Calculate the number of bottles he can buy with the refund
    bottles_with_refund = total_refund / 3.00  # each bottle costs $3.00

    result = bottles_with_refund
    return result

print(solution())