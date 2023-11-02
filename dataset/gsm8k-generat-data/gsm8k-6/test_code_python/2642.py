def solution():
    # Find how much money George spent on the shirt
    spent_on_shirt = 100 - 65  # George had $65 left after buying the shirt, so he spent $100 - $65 = $35 on the shirt

    # Find how much money George spent on the pair of socks
    spent_on_socks = spent_on_shirt - 24  # George spent $24 on the shirt, so he spent $35 - $24 = $11 on the pair of socks

    result = spent_on_socks
    return result

print(solution())