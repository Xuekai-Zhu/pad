def solution():
    charge_time = 45  # initial charge time in minutes
    initial_charge = 0  # initial charge in percentage
    final_charge = 100  # final charge in percentage
    time_to_charge = (final_charge - initial_charge) * (charge_time / 25)  # calculate the additional time needed to reach 100% charge
    result = time_to_charge
    return result

print(solution())