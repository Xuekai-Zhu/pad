def solution():
    """Paul made two bank transfers of $90 and $60 respectively. A service charge of 2% was added to each transaction. If the second transaction was reversed (without the service charge), what is his account balance now if it was $400 before he made any of the transfers?"""
    # Define the initial account balance
    initial_balance = 400

    # Define the transfer amounts
    transfer1 = 90
    transfer2 = 60

    # Calculate the total service charge for both transfers
    service_charge = (transfer1 + transfer2) * 0.02

    # Calculate the total amount transferred
    total_transfer = transfer1 + transfer2 + service_charge

    # Reverse the second transaction (without the service charge)
    total_transfer -= (transfer2 * 0.98)

    # Calculate the new account balance
    new_balance = initial_balance - total_transfer

    # Display the new account balance
    result = new_balance
    return result

print(solution())