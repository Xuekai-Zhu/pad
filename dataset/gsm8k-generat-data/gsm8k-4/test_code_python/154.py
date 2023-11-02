def solution():
    """Ariella has $200 more in her son's saving account than Daniella has in her son's savings account. Ariella's account earns her simple interest at the rate of 10% per annum. If Daniella has $400, how much money will Arialla have after two years?"""
    # Define Daniella's initial amount and Ariella's initial amount (which is $200 more)
    daniella_initial = 400
    ariella_initial = daniella_initial + 200

    # Calculate Ariella's account balance after 2 years with simple interest
    ariella_balance = ariella_initial * (1 + 0.1 * 2)

    # return the result
    result = ariella_balance
    return result

print(solution())