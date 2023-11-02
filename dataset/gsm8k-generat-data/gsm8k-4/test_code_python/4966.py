def solution():
    """Paul made two bank transfers of $90 and $60 respectively. A service charge of 2% was added to each transaction. If the second transaction was reversed (without the service charge), what is his account balance now if it was $400 before he made any of the transfers?"""
    # Define the initial account balance and the service charge rate
    INITIAL_BALANCE = 400
    SERVICE_CHARGE_RATE = 0.02

    # Calculate the service charge for the two transactions
    service_charge = (90 + 60) * SERVICE_CHARGE_RATE

    # Calculate the total amount transferred, including service charges
    total_transferred = 90 + 60 + service_charge * 2

    # Calculate the final account balance, if the second transaction is reversed
    final_balance = INITIAL_BALANCE - total_transferred + 60

    # return the result
    result = final_balance
    return result

print(solution())