def solution():
    starting_money = 30
    lunch_cost = 10

    # Calculate the money Randy has left after buying lunch
    remaining_money = starting_money - lunch_cost

    # Calculate the amount spent on the ice cream cone
    ice_cream_cost = remaining_money / 4

    # Calculate the money Randy has left after buying lunch and the ice cream cone
    final_money = remaining_money - ice_cream_cost
    result = final_money
    return result

print(solution())