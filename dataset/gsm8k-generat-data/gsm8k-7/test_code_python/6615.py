def solution():
    pete_money = 2.50
    raymond_money = 2.50
    pete_spending = 4 * 5  # 4 nickels = 20 cents
    raymond_spending = (2.50 - 0.70) * 100  # 7 dimes = 70 cents, convert remaining money to cents

    # Calculate the total amount spent by both Pete and Raymond
    total_spending = pete_spending + raymond_spending
    result = total_spending
    return result

print(solution())