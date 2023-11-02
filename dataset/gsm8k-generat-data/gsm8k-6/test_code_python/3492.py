def solution():
    # Calculate the total amount of money in Samuel's wallet
    total_money = 5*x + 10*y + 20*z

    # Solve for y using the given information that his $10-bills amount to $50
    y = 5

    # Solve for z using the given information that he has 4 $20-bills
    z = 4

    # Solve for x using the equation total_money = $150
    x = (150 - 10*y - 20*z) / 5

    # Calculate the total number of bills in Samuel's wallet
    total_bills = x + y + z
    result = total_bills
    return result

print(solution())