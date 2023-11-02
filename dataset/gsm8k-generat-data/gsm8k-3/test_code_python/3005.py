def solution():
    """Aitana and Jayda went to Silverlake Flea market to buy some handmade crafts. Aitana spent 2/5 times more money than Jayda at the market. If Jayda spent $400, calculate the total amount of money they spent together."""
    # Define the amount of money Jayda spent
    jayda_spent = 400

    # Calculate the amount of money Aitana spent
    aitana_spent = jayda_spent * (2/5 + 1)

    # Calculate the total amount of money they spent together
    total_spent = jayda_spent + aitana_spent

    # Display the total amount of money they spent together
    result = total_spent
    return result

print(solution())