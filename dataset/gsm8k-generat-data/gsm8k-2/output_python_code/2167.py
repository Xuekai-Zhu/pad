def solution():
    """Since the 40th president launched his reelection campaign today, he has raised $10,000 in campaign funds. His friends raised 40% of this amount and his family raised 30% of the remaining amount. The rest of the funds are from his own savings for the election. How much did he save for the presidency?"""
    total_funds = 10000
    friends_share = 0.4 * total_funds
    remaining_funds = total_funds - friends_share
    family_share = 0.3 * remaining_funds
    own_savings = remaining_funds - family_share
    result = own_savings
    return result

print(solution())