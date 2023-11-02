def solution():
    # Calculate the total cost of the purchase
    total_cost = 2*5 + 3*4 + 2*2  # 2 posters cost $10, 3 notebooks cost $12, 2 bookmarks cost $4

    # Calculate how much money Whitney will have left over
    money_left = (2*20) - total_cost  # Whitney was given two $20 bills to spend
    result = money_left
    return result

print(solution())