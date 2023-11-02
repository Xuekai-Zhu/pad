def solution():
    fiat_money = True
    intrinsic_value = False
    pound_to_dollar_rate = 1.24
    if fiat_money and not intrinsic_value and pound_to_dollar_rate > 0:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())