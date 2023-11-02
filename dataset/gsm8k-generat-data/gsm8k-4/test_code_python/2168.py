def solution():
    """Since the 40th president launched his reelection campaign today, he has raised $10,000 in campaign funds. His friends raised 40% of this amount and his family raised 30% of the remaining amount. The rest of the funds are from his own savings for the election. How much did he save for the presidency?"""
    # Define the initial amount raised
    total_raised = 10000

    # Calculate the amount raised by the president's friends
    friends_raised = total_raised * 0.4

    # Calculate the remaining amount after friends' contribution
    remaining_amount = total_raised - friends_raised

    # Calculate the amount raised by the president's family
    family_raised = remaining_amount * 0.3

    # Calculate the amount saved by the president for the campaign
    savings_amount = total_raised - friends_raised - family_raised

    # return the result
    result = savings_amount
    return result

print(solution())