def solution():
    """Gina has two bank accounts. Each account has a quarter of the balance in Betty's account. If Betty's account balance is $3,456, what is the combined balance of both Gina's accounts?"""
    betty_balance = 3456
    gina_balance = betty_balance / 4
    
    combined_balance = gina_balance * 2
    
    result = combined_balance
    return result

print(solution())