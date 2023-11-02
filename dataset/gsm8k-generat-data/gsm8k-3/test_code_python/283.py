def solution():
    """Gina has two bank accounts. Each account has a quarter of the balance in Betty's account. If Betty's account balance is $3,456, what is the combined balance of both Gina's accounts?"""
    # Define Betty's account balance
    betty_balance = 3456

    # Calculate the balance of each of Gina's accounts
    gina_balance = betty_balance / 4
    total_balance = gina_balance * 2

    # Display the combined balance of Gina's accounts
    result = total_balance
    return result

print(solution())