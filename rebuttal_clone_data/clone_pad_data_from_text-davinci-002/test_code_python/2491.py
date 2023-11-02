def solution():
    fudge_sold = 20
    fudge_price = 2.50
    truffles_sold = 5
    truffles_price = 1.50
    pretzels_sold = 3
    pretzels_price = 2.00
    
    total_fudge_price = fudge_sold * fudge_price
    total_truffle_price = truffles_sold * truffles_price
    total_pretzel_price = pretzels_sold * pretzels_price
    
    total_price = total_fudge_price + total_truffle_price + total_pretzel_price
    
    return total_price

print(solution())