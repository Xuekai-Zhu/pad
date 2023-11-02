def solution():
    amount_paid = 2 * 20 + 4 * 10  # total amount of cash Pete has
    amount_left = 90 - amount_paid  # amount of money needed to pay off the bike
    num_bottles = int(amount_left / 0.5)  # number of bottles Pete needs to return, rounding down
    result = num_bottles
    return result

print(solution())