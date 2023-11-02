def solution():
    budget = 90
    arcade_tokens = 5
    mini_golf_price = 5
    go_kart_price = 10

    # Calculate the total cost of the mini-golf rides
    mini_golf_cost = mini_golf_price * 2

    # Calculate the total cost of the go-karts
    go_kart_cost = go_kolf_cost * 2

    # Calculate the remaining budget after the arcade tokens
    remaining_budget = budget - arcade_tokens - mini_golf_cost

    # Calculate the number of friends Morgan can invite
    num_friends = remaining_budget // go_kart_cost
    result = num_friends
    return result

print(solution())