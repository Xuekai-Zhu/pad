def solution():
    barry_total = 10.00
    dan_total = barry_total / 2 + 0.2  # Dan has half of Barry's total plus 2 more dimes
    num_dimes = dan_total / 0.10  # Each dime has a value of $0.10
    result = num_dimes
    return result

print(solution())