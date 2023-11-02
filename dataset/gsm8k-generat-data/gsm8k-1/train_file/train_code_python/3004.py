def solution():
    """Aitana and Jayda went to Silverlake Flea market to buy some handmade crafts. Aitana spent 2/5 times more money than Jayda at the market. If Jayda spent $400, calculate the total amount of money they spent together."""
    jayda_spent = 400
    aitana_spent = jayda_spent * (2/5) + jayda_spent
    total_spent = aitana_spent + jayda_spent
    result = total_spent
    return result

print(solution())