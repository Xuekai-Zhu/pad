def solution():
    """Last month, you borrowed $100 from your friend. If you promise to pay her today, how much will you give to your friend if both of you agreed to return the money with a 10% increase?"""
    borrowed_amount = 100
    increase_percentage = 10
    increase_amount = borrowed_amount * (increase_percentage / 100)
    total_amount = borrowed_amount + increase_amount
    result = total_amount
    return result

print(solution())