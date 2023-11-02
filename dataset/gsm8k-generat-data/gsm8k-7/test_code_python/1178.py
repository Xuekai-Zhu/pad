def solution():
    oula_deliveries = 96
    tona_deliveries = oula_deliveries * (3/4)

    oula_pay = oula_deliveries * 100
    tona_pay = tona_deliveries * 100

    diff_in_pay = oula_pay - tona_pay
    result = diff_in_pay
    return result

print(solution())