def solution():
    """Mr. Smith has incurred a 2% finance charge because he was not able to pay on time for his balance worth $150. If he plans to settle his balance today, how much will Mr. Smith pay?"""
    # Define the original balance and the finance charge rate
    original_balance = 150
    finance_charge_rate = 0.02

    # Calculate the finance charge
    finance_charge = original_balance * finance_charge_rate

    # Calculate the total amount due
    total_due = original_balance + finance_charge

    # Display the total amount due
    result = total_due
    return result

print(solution())