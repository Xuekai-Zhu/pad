def solution():
    # Calculate the value of 20 quarters through dimes
    dimes_per_quarter = 3
    value_per_dime = 0.10
    quarters_through_dimes = 20
    total_dimes = quarters_through_dimes * dimes_per_quarter
    value_through_dimes = total_dimes * value_per_dime
    value_per_quarter = 0.25
    value_with_dimes = quarters_through_dimes * value_per_quarter

    # Calculate the value of 20 quarters through nickels
    nickels_per_quarter = 7
    value_per_nickel = 0.05
    quarters_through_nickels = 20
    total_nickels = quarters_through_nickels * nickels_per_quarter
    value_through_nickels = total_nickels * value_per_nickel
    value_per_quarter = 0.25
    value_with_nickels = quarters_through_nickels * value_per_quarter

    total_loss = (value_with_dimes + value_with_nickels) - (value_through_dimes + value_through_nickels)
    result = total_loss
    return result

print(solution())