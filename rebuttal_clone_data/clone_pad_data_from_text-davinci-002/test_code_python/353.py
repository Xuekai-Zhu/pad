def solution():
    total_cost = 20700
    cost_per_item = 134
    number_of_items = total_cost / cost_per_item
    overcharge_amount = number_of_items * 10
    reimbursement = total_cost - overcharge_amount
    result = reimbursement
    return result

print(solution())