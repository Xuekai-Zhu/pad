def solution():
    """Gina has two bank accounts. Each account has a quarter of the balance in Betty's account. If Betty's account balance is $3,456, what is the combined balance of both Gina's accounts?"""
    betty_balance = 3456
    gina_balance = (1/4) * betty_balance
    total_balance = 2 * gina_balance
    result = total_balance
    return result

print(solution())