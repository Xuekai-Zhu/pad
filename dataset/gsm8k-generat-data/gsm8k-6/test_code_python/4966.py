def solution():
    initial_balance = 400
    first_transfer = 90
    second_transfer = 60
    service_charge_rate = 0.02

    # Calculate the amounts after service charges for both transfers
    charged_first = first_transfer + (first_transfer * service_charge_rate)
    charged_second = second_transfer + (second_transfer * service_charge_rate)

    # Calculate the new balance after both transfers, but only reversing the second transfer
    new_balance = initial_balance - charged_first + (second_transfer * (1 - service_charge_rate))

    result = new_balance
    return result

print(solution())