def solution():
    
    melisa_tip_percentage = 15
    jennifer_tip_percentage = 20
    melisa_tip_amount = 42
    bill_amount = melisa_tip_amount / (melisa_tip_percentage / 100)
    jennifer_tip_amount = bill_amount * (jennifer_tip_percentage / 100)
    result = jennifer_tip_amount
    return result

print(solution())