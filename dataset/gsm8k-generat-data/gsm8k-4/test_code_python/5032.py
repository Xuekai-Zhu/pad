def solution():
    """A portable battery charger can fully charge a smartphone in 26 minutes or a tablet in 53 minutes. Ana charged her tablet fully and her phone halfway. How many minutes did it take?"""
    # Define the times to fully charge a smartphone and a tablet
    smartphone_time = 26
    tablet_time = 53

    # Calculate the time to charge Ana's tablet
    tablet_charge_time = tablet_time

    # Calculate the time to charge Ana's phone halfway
    phone_charge_time = smartphone_time / 2

    # Calculate the total time it took to charge Ana's devices
    total_charge_time = tablet_charge_time + phone_charge_time

    # return the result
    result = total_charge_time
    return result

print(solution())