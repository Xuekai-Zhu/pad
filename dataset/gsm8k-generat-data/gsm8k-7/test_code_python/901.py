def solution():
    sandi_money = 600
    
    # Calculate how much Sandi spent
    sandi_spent = sandi_money / 2

    # Calculate Gillian's total spent
    gillian_spent = 3 * sandi_spent + 150
    result = gillian_spent - sandi_spent  # Get the portion spent at the farmer's market
    return result

print(solution())