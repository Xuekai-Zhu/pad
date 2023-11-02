def solution():
    # Calculate how much Sandi spent at the farmer's market
    sandi_spent = 600 / 2

    # Calculate Gillian's total spent
    gillian_spent = 150 + 3 * sandi_spent

    # Calculate how much Gillian spent at the farmer's market
    gillian_at_market = gillian_spent - (600/2)

    result = gillian_at_market
    return result

print(solution())