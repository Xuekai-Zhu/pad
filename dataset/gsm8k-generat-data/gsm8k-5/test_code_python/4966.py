def solution():
    initial_balance = 400  # Paul's initial account balance
    transfer1 = 90 * 1.02  # The first transfer with a service charge
    transfer2_reversed = 60  # The second transfer without the service charge
    transfer2 = transfer2_reversed / 1.02  # The second transfer with the service charge

    # Calculate the new account balance after both transfers and the reversal
    new_balance = initial_balance - transfer1 - transfer2 + transfer2_reversed
    result = new_balance
    return result

print(solution())