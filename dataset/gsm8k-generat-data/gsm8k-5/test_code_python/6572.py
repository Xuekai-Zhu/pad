def solution():
    initial_amount = 20  # Josh starts with $20
    hat_cost = 10
    pencil_cost = 2
    num_cookies = 4
    cost_per_cookie = 1.25

    # Calculate Josh's total expenditure
    total_spent = hat_cost + pencil_cost + (num_cookies * cost_per_cookie)

    # Calculate how much money Josh has left
    money_left = initial_amount - total_spent
    result = money_left
    return result

print(solution())