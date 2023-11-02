def solution():
    starting_money = 100  # George started with $100
    shirt_cost = 24  # George spent $24 on a shirt
    remaining_money = 65  # George had $65 left after buying the shirt and socks

    # Calculate how much George spent on the socks
    sock_cost = starting_money - shirt_cost - remaining_money
    result = sock_cost
    return result

print(solution())