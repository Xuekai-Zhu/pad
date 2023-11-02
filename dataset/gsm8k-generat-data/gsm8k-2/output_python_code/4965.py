def solution():
    """Paul made two bank transfers of $90 and $60 respectively. A service charge of 2% was added to each transaction. If the second transaction was reversed (without the service charge), what is his account balance now if it was $400 before he made any of the transfers?"""
    start_balance = 400
    transfer_1 = 90
    transfer_2 = 60
    service_charge = 0.02
    new_balance = start_balance - transfer_1 - (transfer_2 * (1 + service_charge))
    result = new_balance
    return result

print(solution())