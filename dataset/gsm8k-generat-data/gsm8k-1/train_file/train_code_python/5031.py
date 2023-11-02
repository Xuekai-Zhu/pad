def solution():
    """A portable battery charger can fully charge a smartphone in 26 minutes or a tablet in 53 minutes. Ana charged her tablet fully and her phone halfway. How many minutes did it take?"""
    phone_charge_time = 26/2 # half the time to fully charge
    tablet_charge_time = 53
    total_charge_time = phone_charge_time + tablet_charge_time
    result = total_charge_time
    return result

print(solution())