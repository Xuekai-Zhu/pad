def solution():
    betty_balance = 3456  # Betty's account balance is $3,456
    gina_balance = betty_balance / 4  # Each of Gina's accounts has a quarter of Betty's balance
    combined_balance = gina_balance * 2  # Gina has two accounts, so their balances are added together
    result = combined_balance
    return result

print(solution())