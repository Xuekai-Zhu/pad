def solution():
    # Define John's initial investment, interest rate, and time
    principal = 1000
    rate = 0.1
    time = 3

    # Calculate the interest earned
    interest = principal * rate * time

    # Calculate the final amount
    final_amount = principal + interest
    result = final_amount
    return result

print(solution())