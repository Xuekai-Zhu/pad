def solution():
    # Liza started with $800 in her checking account
    checking_account_balance = 800

    # Liza paid her rent on Wednesday
    checking_account_balance -= 450

    # Liza deposited her paycheck on Thursday
    checking_account_balance += 1500

    # Liza paid her electricity and internet bills on Friday
    checking_account_balance -= 117
    checking_account_balance -= 100

    # Liza paid her phone bill on Saturday
    checking_account_balance -= 70

    result = checking_account_balance
    return result

print(solution())