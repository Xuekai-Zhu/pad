def solution():
    """Tom finds 10 quarters, 3 dimes, and 4 nickels and 200 pennies. In dollars, how much money did he find?"""
    quarter_value = 0.25
    dime_value = 0.1
    nickel_value = 0.05
    penny_value = 0.01
    total_value = (10 * quarter_value) + (3 * dime_value) + (4 * nickel_value) + (200 * penny_value)
    result = total_value
    return result

print(solution())