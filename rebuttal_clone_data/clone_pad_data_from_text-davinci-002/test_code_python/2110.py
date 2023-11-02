def solution():
    cost_of_snickers = 1.5
    cost_of_mms = cost_of_snickers * 2
    snickers_bought = 2
    mms_bought = 3
    total_cost = (snickers_bought * cost_of_snickers) + (mms_bought * cost_of_mms)
    cash_given = 20
    change = cash_given - total_cost
    result = change
    return result

print(solution())