def solution():
    # Define the value of the quarters, dimes, and nickel in cents
    quarter_value = 25
    dime_value = 10
    nickel_value = 5

    # Calculate the total value of John's payment in cents
    payment_total = 4 * quarter_value + 3 * dime_value + 1 * nickel_value

    # Subtract the change received from the payment total to find the cost of the candy bar
    candy_bar_cost = payment_total - 4
    result = candy_bar_cost
    return result

print(solution())