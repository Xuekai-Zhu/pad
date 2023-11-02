def solution():
    # Calculate the number of water bottles Lilith had
    num_bottles = 5 * 12  # five dozen water bottles

    # Calculate the original price Lilith planned to sell the water bottles for
    orig_price = 2  # $2 per water bottle

    # Calculate the reduced price that Lilith had to sell the water bottles for
    reduced_price = 1.85  # $1.85 per water bottle

    # Calculate the total amount of money Lilith will make after selling all her water bottles
    total_money = num_bottles * reduced_price

    # Calculate the amount of money Lilith will have to find for the birthday gift after selling the water bottles
    gift_cost = total_money - (num_bottles * orig_price)

    result = gift_cost
    return result

print(solution())