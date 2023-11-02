def solution():
    apples_eaten_Tuesday = 4
    apples_eaten_Wednesday = apples_eaten_Tuesday * 2
    apples_eaten_Thursday = apples_eaten_Tuesday / 2
    total_apples = apples_eaten_Tuesday + apples_eaten_Wednesday + apples_eaten_Thursday
    result = total_apples
    return result

print(solution())