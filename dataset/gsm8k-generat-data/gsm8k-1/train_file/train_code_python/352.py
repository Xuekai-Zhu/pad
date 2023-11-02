def solution():
    """On Friday, Remy paid Sally’s Woodworking LLC a total of $20,700 for 150 pieces of furniture. Later that evening, the company’s accountant discovered that a new intern in the sales department had overcharged Remy. If the cost of a piece of furniture is $134, how much money will Sally’s Woodworking LLC reimburse Remy?"""
    total_cost = 20700
    cost_per_piece = 134
    actual_cost = cost_per_piece * 150
    refund_amount = total_cost - actual_cost
    result = refund_amount
    
    return result

print(solution())