def solution():
    # Define the fraction of money Anna spent
    fraction_spent = 1/4

    # Calculate the amount of money Anna has left
    left_money = 24

    # Calculate the original amount of money Anna had
    original_money = left_money / (1 - fraction_spent)
    result = original_money
    return result

print(solution())