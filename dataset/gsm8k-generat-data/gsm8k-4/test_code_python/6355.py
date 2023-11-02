def solution():
    """Louis is making himself a velvet suit for a formal event. The velvet fabric he chose was $24 per yard. He bought a pattern for $15, and two spools of silver thread for $3 each. If he spent $141 for the pattern, thread, and fabric, how many yards of fabric did he buy?"""
    # Define the price of the velvet fabric per yard and the cost of the pattern
    fabric_price_per_yard = 24
    pattern_cost = 15

    # Define the cost of the two spools of silver thread
    thread_cost = 2 * 3

    # Define the total amount spent
    total_cost = 141

    # Calculate the amount spent on the fabric
    fabric_cost = total_cost - pattern_cost - thread_cost

    # Calculate the number of yards of fabric purchased
    yards_purchased = fabric_cost / fabric_price_per_yard

    # round the result
    result = round(yards_purchased, 2)
    return result

print(solution())