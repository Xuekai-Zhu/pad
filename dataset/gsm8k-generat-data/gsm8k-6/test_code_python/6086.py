def solution():
    # Calculate the total cost of the candy bars
    candy_bar_cost = 1.5  # cost of one candy bar
    candy_bars_bought = 20  # total candy bars bought
    candy_bars_paid_by_Dave = 6  # candy bars paid by Dave
    total_cost = (candy_bars_bought - candy_bars_paid_by_Dave) * candy_bar_cost

    # Calculate how much John paid
    john_paid = total_cost
    result = john_paid
    return result

print(solution())