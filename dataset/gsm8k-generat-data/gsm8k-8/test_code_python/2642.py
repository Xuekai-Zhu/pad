def solution():
    starting_money = 100
    shirt_cost = 24
    ending_money = 65

    # Calculate the total cost of the shirt and socks
    total_cost = starting_money - ending_money
    sock_cost = total_cost - shirt_cost
    result = sock_cost
    return result

print(solution())