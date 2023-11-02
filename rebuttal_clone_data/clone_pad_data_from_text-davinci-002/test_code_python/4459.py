def solution():
    quarters = 10
    dimes = 12
    total_coins = quarters + dimes
    total_value = quarters * 0.25 + dimes * 0.1
    nickel_value = 0.05
    num_nickels = (4 - total_value) / nickel_value
    result = num_nickels
    return result

print(solution())