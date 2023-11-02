def solution():
    original_balance = 400
    transfer_1 = 90
    transfer_2 = 60
    service_charge_rate = 0.02

    # Calculate the service charge for the first transfer
    transfer_1_charge = transfer_1 * service_charge_rate

    # Calculate the total amount debited from the account after the first transfer
    total_debit_1 = transfer_1 + transfer_1_charge

    # Calculate the service charge for the second transfer
    transfer_2_charge = transfer_2 * service_charge_rate

    # Calculate the total amount credited back to the account after the second transfer was reversed
    total_credit_2 = transfer_2 - transfer_2_charge

    # Calculate the total amount debited from the account after both transfers and service charges
    total_debit = total_debit_1 + transfer_2 + transfer_2_charge

    # Calculate the final account balance
    final_balance = original_balance - total_debit + total_credit_2
    result = final_balance
    return result

print(solution())