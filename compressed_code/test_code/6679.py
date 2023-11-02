def solution():
    
    tulip_bulbs = 20
    iris_bulbs = tulip_bulbs / 2
    daffodil_bulbs = 30
    crocus_bulbs = 3 * daffodil_bulbs
    
    total_bulbs = tulip_bulbs + iris_bulbs + daffodil_bulbs + crocus_bulbs
    pay_per_bulb = 0.5
    total_pay = total_bulbs * pay_per_bulb
    result = total_pay
    
    return result

print(solution())