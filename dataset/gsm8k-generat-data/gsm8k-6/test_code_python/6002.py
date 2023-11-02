def solution():
    # Calculate the amount spent on food and travel expenses in a month
    expenses = 1200 * 2  # rent was half of what was spent on food and travel expenses

    # Calculate the total amount earned by Kathryn in a month
    total_salary = 5000

    # Calculate the amount remaining after subtracting the expenses and splitting rent with Shelby
    remaining_money = total_salary - (expenses/2 + 1200/2)
    result = remaining_money
    return result

print(solution())