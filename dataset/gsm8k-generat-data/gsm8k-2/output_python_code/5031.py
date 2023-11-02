def solution():
    """A portable battery charger can fully charge a smartphone in 26 minutes or a tablet in 53 minutes. Ana charged her tablet fully and her phone halfway. How many minutes did it take?"""
    tablet_charge_time = 53
    smartphone_charge_time = 26
    ana_tablet_time = tablet_charge_time
    ana_phone_time = smartphone_charge_time / 2
    total_charge_time = ana_tablet_time + ana_phone_time
    result = total_charge_time
    return result

print(solution())