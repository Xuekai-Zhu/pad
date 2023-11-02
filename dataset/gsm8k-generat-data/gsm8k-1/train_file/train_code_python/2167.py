def solution():
    """Since the 40th president launched his reelection campaign today, he has raised $10,000 in campaign funds. His friends raised 40% of this amount and his family raised 30% of the remaining amount. The rest of the funds are from his own savings for the election. How much did he save for the presidency?"""
    initial_funds = 10000
    friends_percent = 0.4
    family_percent = 0.3
    friends_share = initial_funds * friends_percent
    remaining_funds = initial_funds - friends_share
    family_share = remaining_funds * family_percent
    savings = initial_funds - friends_share - family_share
    result = savings
    return result

print(solution())