def solution():
    """On Tuesday, Liza had $800 in her checking account. On Wednesday, she paid her rent, $450. On Thursday, she deposited her $1500 paycheck. On Friday, she paid her electricity and internet bills which were $117 and $100, respectively. Then on Saturday, she paid her phone bill, $70. How much money is left in Liza's account?"""
    # Define the initial balance
    balance = 800

    # Subtract the rent paid on Wednesday
    balance -= 450

    # Add the paycheck deposited on Thursday
    balance += 1500

    # Subtract the electricity and internet bills paid on Friday
    balance -= 117
    balance -= 100

    # Subtract the phone bill paid on Saturday
    balance -= 70

    # Return the remaining balance
    result = balance
    return result

print(solution())