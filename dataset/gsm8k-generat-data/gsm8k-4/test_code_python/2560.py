def solution():
    """Mr. Smith has incurred a 2% finance charge because he was not able to pay on time for his balance worth $150. If he plans to settle his balance today, how much will Mr. Smith pay?"""
    # Define the initial balance
    balance = 150

    # Calculate the finance charge
    finance_charge = balance * 0.02

    # Calculate the total amount to be paid
    total_amount = balance + finance_charge

    # return the result
    result = total_amount
    return result

print(solution())