def solution():
    barry_money = 10.00  # Barry has $10.00 worth of dimes
    barry_dimes = barry_money / 0.10  # Number of dimes Barry has

    dan_money = barry_money / 2  # Dan has half the amount of Barry
    dan_dimes = (dan_money + 0.20) / 0.10  # Dan found 2 more dimes on his way home
    result = dan_dimes
    return result

print(solution())