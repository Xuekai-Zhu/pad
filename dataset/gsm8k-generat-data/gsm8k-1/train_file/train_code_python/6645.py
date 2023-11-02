def solution():
    """Mrs. Brown paid her utility bills with 3 $50 bills and 2 $10 bills. How much are her utility bills?"""
    num_fifty_bills = 3
    num_ten_bills = 2
    value_of_fifty_bills = num_fifty_bills * 50
    value_of_ten_bills = num_ten_bills * 10
    total_cost = value_of_fifty_bills + value_of_ten_bills
    result = total_cost
    return result

print(solution())