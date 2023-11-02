def solution():
    """Mrs. Brown paid her utility bills with 3 $50 bills and 2 $10 bills. How much are her utility bills?"""
    total_50_bills = 3
    total_10_bills = 2
    value_of_50_bills = 50 * total_50_bills
    value_of_10_bills = 10 * total_10_bills
    total_bills = value_of_50_bills + value_of_10_bills
    result = total_bills
    return result

print(solution())