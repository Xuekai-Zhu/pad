def solution():
    """Samuel has $5, $10, and $20 bills which amount to $150 in his wallet. His $10-bills amount to $50, and he has 4 $20-bills. How many bills does Samuel have in his wallet?"""
    # Define the amount of money in Samuel's wallet
    wallet_total = 150

    # Define the number of $10 bills Samuel has
    num_10_bills = 5

    # Define the number of $20 bills Samuel has
    num_20_bills = 4

    # Calculate the number of $5 bills Samuel has
    num_5_bills = (wallet_total - (num_10_bills * 10) - (num_20_bills * 20)) / 5

    # Calculate the total number of bills Samuel has
    total_bills = num_5_bills + num_10_bills + num_20_bills

    result = total_bills
    return result

print(solution())