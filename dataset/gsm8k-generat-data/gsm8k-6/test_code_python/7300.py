def solution():
    # Calculate the amount of money John spent walking the dog
    daily_cost = 10/26  # John walks the dog for 26 days in April (excluding the 4 Sundays)
    total_dog_cost = daily_cost * 26  # total amount spent walking the dog
    total_spent = total_dog_cost + 50 + 50  # total amount spent on books and giving money to his sister Kaylee
    starting_money = 100  # assuming John started with $100
    money_left = starting_money - total_spent  # calculate the amount of money John has left
    result = money_left
    return result

print(solution())