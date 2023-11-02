def solution():
    """Gina has two bank accounts. Each account has a quarter of the balance in Betty's account. If Betty's account balance is $3,456, what is the combined balance of both Gina's accounts?"""
    # Define Betty's account balance
    betty_balance = 3456

    # Calculate the balance in each of Gina's accounts
    gina_balance = betty_balance / 4

    # Calculate the combined balance of both of Gina's accounts
    combined_balance = gina_balance * 2

    # return the result
    result = combined_balance
    return result

print(solution())