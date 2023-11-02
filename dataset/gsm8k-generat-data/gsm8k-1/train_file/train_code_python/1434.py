def solution():
    """When Harriett vacuumed the sofa and chair she found 10 quarters, 3 dimes, 3 nickels, and 5 pennies. How much money did Harriett find?"""
    quarters = 10
    dimes = 3
    nickels = 3
    pennies = 5
    total_amount = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    result = total_amount
    return result

print(solution())