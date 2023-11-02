def solution():
    start_amount = 500  # Lucy had 500g of flour in the cupboard at the start of the week
    used_amount = 240  # Lucy used 240g of flour to bake cookies on Tuesday
    remaining_amount = start_amount - used_amount  # Lucy has this much flour left
    spilled_amount = remaining_amount / 2  # Lucy spilled half of what was left
    current_amount = remaining_amount - spilled_amount  # Lucy currently has this much flour in the cupboard
    required_amount = start_amount - current_amount  # Lucy needs to buy this much flour to have a full bag

    result = required_amount
    return result

print(solution())