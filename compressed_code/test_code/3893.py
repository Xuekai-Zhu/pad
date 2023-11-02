def solution():
    
    tablet_charge_time = 53
    smartphone_charge_time = 26
    ana_tablet_time = tablet_charge_time
    ana_phone_time = smartphone_charge_time / 2
    total_charge_time = ana_tablet_time + ana_phone_time
    result = total_charge_time
    return result

print(solution())