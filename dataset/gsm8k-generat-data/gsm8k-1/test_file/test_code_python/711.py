def solution():
    """A company wanted to buy 500 computers and had $700 for each computer. However, when they went to order, they realized the price of each computer was 10% higher than they had planned for. Calculate the total amount of money they paid to buy the computers at the new prices."""
    num_computers = 500
    original_price = 700
    percent_increase = 10
    new_price = original_price + (original_price * percent_increase / 100)
    total_cost = num_computers * new_price
    result = total_cost
    return result

print(solution())