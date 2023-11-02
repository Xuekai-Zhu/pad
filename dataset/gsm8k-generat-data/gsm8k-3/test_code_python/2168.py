def solution():
    """Since the 40th president launched his reelection campaign today, he has raised $10,000 in campaign funds. His friends raised 40% of this amount and his family raised 30% of the remaining amount. The rest of the funds are from his own savings for the election. How much did he save for the presidency?"""
    # Define the total campaign funds raised
    total_funds = 10000

    # Calculate the amount raised by the president's friends
    friends_funds = total_funds * 0.4

    # Calculate the remaining amount after friends' contribution
    remaining_funds = total_funds - friends_funds

    # Calculate the amount raised by the president's family
    family_funds = remaining_funds * 0.3

    # Calculate the amount saved by the president
    president_savings = total_funds - friends_funds - family_funds

    # Display the amount saved by the president
    result = president_savings
    return result

print(solution())