def solution():
    total_candy_bars = 20
    brother_paid_for = 6
    candy_bar_cost = 1.5

    # Calculate the total cost of the candy bars
    total_cost = total_candy_bars * candy_bar_cost

    # Calculate the amount John paid
    john_paid = total_cost - (brother_paid_for * candy_bar_cost)
    result = john_paid
    return result

print(solution())