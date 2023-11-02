def solution():
    # Calculate the total amount of money earned by Bart
    money_Monday = 0.2 * 10 * 3  # Bart finished 3 surveys on Monday, each survey has 10 questions
    money_Tuesday = 0.2 * 10 * 4  # Bart finished 4 surveys on Tuesday, each survey has 10 questions
    total_money = money_Monday + money_Tuesday
    result = total_money
    return result

print(solution())