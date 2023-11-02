def solution():
    phone_charge_time = 26  # Time taken to charge phone fully
    tablet_charge_time = 53  # Time taken to charge tablet fully

    # Ana charged her tablet fully and her phone halfway
    total_charge_time = tablet_charge_time + (phone_charge_time / 2)

    result = total_charge_time
    return result

print(solution())