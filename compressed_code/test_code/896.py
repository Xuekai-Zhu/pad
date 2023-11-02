def solution():
    
    oula_deliveries = 96
    tona_deliveries = 3/4 * oula_deliveries
    oula_pay = oula_deliveries * 100
    tona_pay = tona_deliveries * 100
    pay_difference = oula_pay - tona_pay
    result = pay_difference
    return result

print(solution())