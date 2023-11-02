def solution():
    bought_ Tuesday = 3
    bought_Thursday = 5
    bought_Friday = 2
    left = 4
    eaten = bought_Tuesday + bought_Thursday + bought_Friday - left
    result = eaten
    return result

print(solution())