def solution():
    """Lee mows one lawn and charges $33. Last week he mowed 16 lawns and three customers each gave him a $10 tip. How many dollars did Lee earn mowing lawns last week?"""
    lawn_price = 33
    number_of_lawns = 16
    tip_amount = 10
    total_amount = (lawn_price * number_of_lawns) + (3 * tip_amount)
    result = total_amount
    return result

print(solution())