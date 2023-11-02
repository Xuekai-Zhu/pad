def solution():
    tip_percent = 20
    alicia_sundae = 7.50
    brant_sundae = 10.00
    josh_sundae = 8.50
    yvette_sundae = 9.00
    total_cost = alicia_sundae + brant_sundae + josh_sundae + yvette_sundae
    tip_amount = total_cost * (tip_percent / 100)
    final_bill = total_cost + tip_amount
    result = final_bill
    return result

print(solution())