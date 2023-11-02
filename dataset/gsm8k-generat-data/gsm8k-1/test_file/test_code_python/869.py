def solution():
    """David has $12.48 and wants to buy 16 bolts from a bin at the hardware store. Each bolt costs $0.03. How much money does David have left after paying for the bolts?"""
    starting_amount = 12.48
    bolt_cost = 0.03
    bolt_count = 16
    total_cost = bolt_cost * bolt_count
    remaining_amount = starting_amount - total_cost
    result = remaining_amount
    return result

print(solution())