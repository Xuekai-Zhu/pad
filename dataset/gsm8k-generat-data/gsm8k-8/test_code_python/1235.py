def solution():
    total_money = 20
    sock_cost = 2
    num_sock_pairs = 4
    hat_cost = 7

    total_spent = (sock_cost * num_sock_pairs) + hat_cost
    money_left = total_money - total_spent
    result = money_left
    return result

print(solution())