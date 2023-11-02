def solution():
    """Natalie's father has saved up $10,000 to split up between his kids. Natalie will get half, as she is the oldest. Rick will get 60 percent of the remaining money, and Lucy will get whatever is left after Natalie and Rick get paid. How much money does Lucy get?"""
    # Define the initial amount of money
    initial_money = 10000

    # Calculate Natalie's share
    natalie_share = initial_money / 2

    # Calculate the remaining money
    remaining_money = initial_money - natalie_share

    # Calculate Rick's share
    rick_share = remaining_money * 0.6

    # Calculate Lucy's share
    lucy_share = initial_money - natalie_share - rick_share

    result = lucy_share
    return result

print(solution())