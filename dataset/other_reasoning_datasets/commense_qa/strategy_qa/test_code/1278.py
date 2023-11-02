def solution():
    louvre_value = 45_000_000_000
    george_soros_net_worth = 8_000_000_000
    if louvre_value <= george_soros_net_worth:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())