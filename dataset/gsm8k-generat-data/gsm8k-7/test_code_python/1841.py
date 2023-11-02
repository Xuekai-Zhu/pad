def solution():
    quarters = 20
    dimes = 3 * quarters
    nickels = 7 * quarters
    total_dime_value = 0.1 * dimes
    total_nickel_value = 0.05 * nickels
    total_quarter_cost = 20  # He is willing to pay face value for the quarters
    total_cost = total_dime_value + total_nickel_value - (total_quarter_cost * 0.25)  # He loses value
    result = total_cost
    return result

print(solution())