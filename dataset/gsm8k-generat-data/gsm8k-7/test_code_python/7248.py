def solution():
    current_age = 3
    future_age = current_age * 3
    money_per_year = 5

    # Calculate Mikail's age on his next birthday
    age_on_birthday = current_age + 1

    # Calculate the total amount of money his parents will give him
    total_money = age_on_birthday * money_per_year
    result = total_money
    return result

print(solution())