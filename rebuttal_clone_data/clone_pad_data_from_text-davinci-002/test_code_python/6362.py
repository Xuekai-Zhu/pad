def solution():
    total_money = 360
    money_spent_on_groceries = total_money * 1/5
    money_left = total_money - money_spent_on_groceries
    money_spent_on_magazine = money_left * 1/4
    money_at_first = total_money + money_spent_on_groceries + money_spent_on_magazine
    result = money_at_first
    return result

print(solution())