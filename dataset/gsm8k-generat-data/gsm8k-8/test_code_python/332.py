def solution():
    # Define the amount of money Dorothy earns
    salary = 60000

    # Calculate the amount of taxes she needs to pay
    taxes = 0.18 * salary

    # Calculate the amount of money she will have left
    money_left = salary - taxes
    result = money_left
    return result

print(solution())