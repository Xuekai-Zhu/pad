def solution():
    """Janet works as an exterminator and she also sells molten metal casts of fire ant nests on the Internet. Janet gets paid $70 an hour for exterminator work and makes $20/pound on her ant nest sculptures. If she does 20 hours of exterminator work and sells a 5-pound sculpture and a 7-pound sculpture, how much money does she make?"""
    exterminator_pay = 70 * 20
    sculpture_1_weight = 5
    sculpture_2_weight = 7
    sculpture_1_price = sculpture_1_weight * 20
    sculpture_2_price = sculpture_2_weight * 20
    total_pay = exterminator_pay + sculpture_1_price + sculpture_2_price
    result = total_pay
    return result

print(solution())