def solution():
    candies = 90
    lollipops = candies / 3
    candy_canes = candies - lollipops
    boys = lollipops / 3
    girls = candy_canes / 2
    total = boys + girls
    result = total
    return result

print(solution())