def solution():
    """If Lucy would give Linda $5, Lucy would have the same amount of money as Linda. If Lucy originally had $20, how much money did Linda have at the beginning?"""
    # Define Lucy's original amount of money
    lucy_money = 20

    # Define the amount Lucy would give to Linda
    linda_share = 5

    # Calculate the amount of money both Lucy and Linda would have after the transaction
    total_money = (lucy_money - linda_share) * 2

    # Calculate the amount of money Linda had at the beginning
    linda_money = total_money - lucy_money

    # return the result
    result = linda_money
    return result

print(solution())