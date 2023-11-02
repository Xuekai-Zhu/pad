def solution():
    """Two months ago, Wilson had a total of $150 in his bank account. Then last month, he deposited $17. A few days after, he made a withdrawal. This month, he deposited $21 so he has $16 more than what is in his account two months ago. How much did Wilson withdraw last month?"""
    # Define the initial balance and the amounts deposited and withdrawn
    initial_balance = 150
    deposit1 = 17
    withdrawal = None
    deposit2 = 21

    # Calculate the balance after the first deposit
    balance1 = initial_balance + deposit1

    # Calculate the balance after the withdrawal
    balance2 = balance1 - withdrawal

    # Calculate the balance after the second deposit
    balance3 = balance2 + deposit2

    # Check if the final balance is $16 more than the initial balance
    if balance3 == initial_balance + 16:
        # Calculate the amount withdrawn
        withdrawal = balance1 - initial_balance - deposit2 + 16

    result = withdrawal
    return result

print(solution())