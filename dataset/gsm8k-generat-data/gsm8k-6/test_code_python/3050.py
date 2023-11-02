Solution:
def solution():
    # Calculate the total cost of muffins bought by Janet
    total_cost = 20 - 11  # Janet paid $20 and got $11 in change back
    muffin_cost = 0.75
    muffins_bought = total_cost / muffin_cost  # Each muffin costs 75 cents
    result = muffins_bought
    return result

print(solution())