def solution():
    num_candy_bars = 20
    num_paid_by_dave = 6
    candy_bar_price = 1.5

    # Calculate the total cost of candy bars paid by John
    john_paid = (num_candy_bars - num_paid_by_dave) * candy_bar_price
    result = john_paid
    return result

print(solution())