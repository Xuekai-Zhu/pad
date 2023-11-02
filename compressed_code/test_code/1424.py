def solution():
    
    teagan_pennies = 200
    rex_nickels = 100 * 5
    toni_dimes = 330 * 10
    total_cents = teagan_pennies + rex_nickels + toni_dimes
    total_dollars = total_cents / 100
    result = total_dollars
    return result

print(solution())