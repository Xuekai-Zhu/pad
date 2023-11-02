def solution():
    starting_money = 100
    shirt_price = 24
    remaining_money = 65

    # Calculate the total amount spent on the shirt and socks
    total_spent = starting_money - remaining_money

    # Calculate the cost of the socks
    socks_price = total_spent - shirt_price
    result = socks_price
    return result

print(solution())