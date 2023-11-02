def solution():
    # Calculate how many days John walked the dog in April
    april_days = 30
    sundays = 4
    dog_walking_days = april_days - sundays

    # Calculate how much John earned from dog walking
    daily_pay = 10 / 1  # $10 for 1 hour of dog walking
    total_pay = dog_walking_days * daily_pay

    # Calculate how much money John spent on books and gave to Kaylee
    expenses = 50 + 50

    # Calculate John's remaining money
    remaining_money = total_pay - expenses
    result = remaining_money
    return result

print(solution())