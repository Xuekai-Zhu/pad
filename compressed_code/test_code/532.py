def solution():
    
    lance_cents = 70
    margaret_dollars = 0.75
    margaret_cents = margaret_dollars * 100
    guy_quarters = 2
    guy_dime = 1
    guy_cents = guy_quarters * 25 + guy_dime * 10
    bill_dimes = 6
    bill_cents = bill_dimes * 10
    total_cents = lance_cents + margaret_cents + guy_cents + bill_cents
    result = total_cents
    return result

print(solution())