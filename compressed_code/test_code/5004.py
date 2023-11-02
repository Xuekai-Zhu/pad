def solution():
    
    a_price = 4
    b_price = 3.5
    a_sold = 300
    b_sold = 350
    a_total_earnings = a_price * a_sold
    b_total_earnings = b_price * b_sold
    difference = abs(a_total_earnings - b_total_earnings)
    result = difference
    return result

print(solution())