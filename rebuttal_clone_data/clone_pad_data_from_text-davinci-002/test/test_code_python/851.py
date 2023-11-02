def solution():
    salmon_cost = 40
    burger_cost = 15
    katsu_cost = 25
    service_charge = 10
    tip = 5
    total_bill = salmon_cost + burger_cost + katsu_cost
    service_charge_amount = total_bill * (service_charge / 100)
    tip_amount = total_bill * (tip / 100)
    final_bill = total_bill + service_charge_amount + tip_amount
    change = 100 - final_bill
    result = change
    return result

print(solution())