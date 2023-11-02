def solution():
    pounds = 900000
    exchange_rate = 1.23
    net_worth_in_dollars = pounds * exchange_rate
    if net_worth_in_dollars >= 1000000000:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())