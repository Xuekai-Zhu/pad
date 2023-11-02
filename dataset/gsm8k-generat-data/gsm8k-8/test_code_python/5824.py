def solution():
    barry_dimes = 1000 # $10.00 worth of dimes
    dan_dimes = (barry_dimes / 2) + 20 # Half of Barry's amount plus 2 extra dimes
    result = dan_dimes / 10 # Convert total cents to number of dimes
    return result

print(solution())