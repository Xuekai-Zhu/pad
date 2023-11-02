def solution():
    
    pansies = 5 * 2.5
    hydrangea = 12.5
    petunias = 5 * 1
    subtotal = pansies + hydrangea + petunias
    discount = 0.1 * subtotal
    total = subtotal - discount
    change = 50 - total
    result = change
    return result

print(solution())