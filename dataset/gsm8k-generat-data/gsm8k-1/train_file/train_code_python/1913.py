def solution():
    """Darla needs to pay $4/watt of electricity for 300 watts of electricity, plus a $150 late fee. How much does she pay in total?"""
    watt_rate = 4
    electricity = 300
    late_fee = 150
    total_cost = (watt_rate * electricity) + late_fee
    result = total_cost
    return result

print(solution())