def solution():
    # Calculate the tax amount
    tax = 0.2 * 50

    # Calculate the total deductions
    deductions = tax + 5

    # Calculate the amount Winwin takes home
    take_home = 50 - deductions

    result = take_home
    return result

print(solution())