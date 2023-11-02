def solution():
    
    aryan_debt = 1200
    kyro_debt = aryan_debt / 2
    aryan_payment = aryan_debt * 0.6
    kyro_payment = kyro_debt * 0.8
    total_money = aryan_payment + kyro_payment + 300
    result = total_money
    return result

print(solution())