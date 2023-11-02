def solution():
    total_money = 80
    bill = 3/4 * total_money
    ice_cream_cost = 1.5
    change = 2  # $1 each

    # Calculate how much money they have left after paying the bill
    money_left = total_money - bill

    # Subtract the change they got back from the money left to get their ice cream cost
    ice_cream_cost = (money_left - change*2) / 2

    # Calculate how many scoops of ice cream each person bought
    num_scoops = ice_cream_cost / ice_cream_cost

    result = num_scoops
    return result

print(solution())