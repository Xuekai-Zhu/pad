def solution():
    """Last month, you borrowed $100 from your friend. If you promise to pay her today, how much will you give to your friend if both of you agreed to return the money with a 10% increase?"""
    initial_amount = 100
    percent_increase = 10
    increase_amount = initial_amount * (percent_increase / 100)
    total_amount = initial_amount + increase_amount
    result = total_amount
    return result

print(solution())