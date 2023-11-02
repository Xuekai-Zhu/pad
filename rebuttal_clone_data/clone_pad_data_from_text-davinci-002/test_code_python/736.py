def solution():
    samosa_price = 2
    pakora_price = 3
    lassi_price = 2
    tax_rate = 0.15
    tip_rate = 0.25
    pretax_tip = (samosa_price * 3 + pakora_price * 4 + lassi_price) * tip_rate
    total_bill = (samosa_price * 3 + pakora_price * 4 + lassi_price) + pretax_tip
    tax = total_bill * tax_rate
    result = total_bill + tax
    return result

print(solution())