def solution():
    """Paul made two bank transfers of $90 and $60 respectively. A service charge of 2% was added to each transaction. If the second transaction was reversed (without the service charge), what is his account balance now if it was $400 before he made any of the transfers?"""
    initial_balance = 400
    transfer1 = 90 * 1.02 # add 2% service charge
    transfer2 = 60 * 1.02 # add 2% service charge
    reversed_transfer2 = 60 # without service charge
    new_balance = initial_balance - transfer1 - reversed_transfer2 + transfer2
    result = new_balance
    return result

print(solution())