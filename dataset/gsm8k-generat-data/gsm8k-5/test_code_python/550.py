def solution():
    starting_money = 3000  # Randy starts with $3000
    additional_money = 200  # Smith gives him an additional $200
    total_money = starting_money + additional_money  # Randy now has a total of $3200
    money_spent = 1200  # Randy gives $1200 to Sally
    remaining_money = total_money - money_spent  # Randy keeps the rest of the money
    result = remaining_money
    return result

print(solution())