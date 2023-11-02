def solution():
    """Ariella has $200 more in her son's saving account than Daniella has in her son's savings account. Ariella's account earns her simple interest at the rate of 10% per annum. If Daniella has $400, how much money will Arialla have after two years?"""
    # Define the initial amount in Daniella's account
    daniella_amount = 400

    # Calculate the amount in Ariella's account
    ariella_amount = daniella_amount + 200

    # Calculate the interest earned by Ariella over two years
    interest = ariella_amount * 0.1 * 2

    # Calculate the final amount in Ariella's account
    final_amount = ariella_amount + interest

    # Return the result
    result = final_amount
    return result

print(solution())