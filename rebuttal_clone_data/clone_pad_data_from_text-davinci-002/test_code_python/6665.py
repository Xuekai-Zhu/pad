def solution():
    quarters = 10
    dimes = 3
    nickels = 4
    pennies = 200
    quarter_value = quarters * 0.25
    dime_value = dimes * 0.1
    nickel_value = nickels * 0.05
    penny_value = pennies * 0.01
    total_value = quarter_value + dime_value + nickel_value + penny_value
    result = total_value
    return result

print(solution())