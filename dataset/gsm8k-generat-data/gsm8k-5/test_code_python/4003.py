def solution():
    joanna_money = 8  # Joanna has $8
    brother_money = 3 * joanna_money  # Brother has thrice as much as Joanna
    sister_money = 0.5 * joanna_money  # Sister has half as much as Joanna

    # Calculate the total amount of money the three of them have
    total_money = joanna_money + brother_money + sister_money
    result = total_money
    return result

print(solution())