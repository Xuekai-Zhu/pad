def solution():
    total_money = 2 * 40  # Aaron and Carson each saved $40
    dinner_bill = 3/4 * total_money  # The dinner bill is 3/4 of their total money
    money_left = total_money - dinner_bill  # They have this much money left after dinner
    ice_cream_cost = 1.5  # Each scoop costs $1.5
    money_left -= 2  # They each have $1 in change after buying ice cream

    # Calculate the number of scoops they each bought
    scoops_each = int(money_left / (2 * ice_cream_cost))

    result = scoops_each
    return result

print(solution())