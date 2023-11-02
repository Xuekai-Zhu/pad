def solution():
    robi_contribution = 4000
    rudy_contribution = robi_contribution + (robi_contribution / 4)
    total_contribution = robi_contribution + rudy_contribution
    percent_profit = 20
    profit = total_contribution * (percent_profit / 100)
    split_profit = profit / 2
    result = split_profit
    return result

print(solution())