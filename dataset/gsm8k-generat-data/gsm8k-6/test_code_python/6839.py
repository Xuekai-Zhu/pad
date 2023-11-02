def solution():
    # Calculate the total amount of money Rachel spent
    lunch_cost = (1/4) * 200  # Rachel spent 1/4 of the money on lunch
    DVD_cost = (1/2) * 200  # Rachel spent 1/2 of the money on a DVD
    total_spent = lunch_cost + DVD_cost

    # Calculate how much money Rachel has left
    money_left = 200 - total_spent
    result = money_left
    return result

print(solution())