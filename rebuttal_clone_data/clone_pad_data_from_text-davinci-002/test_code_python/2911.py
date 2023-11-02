def solution():
    bars_bought = 20
    bars_kept = 1
    bars_traded = 3
    bars_given = bars_bought - bars_kept - bars_traded
    bars_given_per_sister = bars_given / 2
    result = bars_given_per_sister
    return result

print(solution())