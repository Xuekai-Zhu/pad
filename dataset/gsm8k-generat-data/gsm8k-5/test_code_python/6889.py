def solution():
    # Ben's initial amount
    initial_amount = 2000
    
    # The cheque he writes to his supplier
    supplier_payment = 600
    
    # The payment he receives from his debtor
    debtor_payment = 800
    
    # The amount he spends on equipment maintenance
    maintenance_cost = 1200
    
    # Calculate his remaining balance
    remaining_balance = initial_amount - supplier_payment + debtor_payment - maintenance_cost
    
    result = remaining_balance
    return result

print(solution())