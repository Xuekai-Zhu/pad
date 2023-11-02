def solution():
    total_milk = 16
    butter = total_milk * 0.25
    sour_cream = total_milk * 0.25
    remaining = total_milk - butter - sour_cream
    butter_gallons = butter / 4
    sour_cream_gallons = sour_cream / 2

    money_from_butter = butter_gallons * 5
    money_from_sour_cream = sour_cream_gallons * 6
    money_from_whole_milk = remaining * 3

    total_money = money_from_butter + money_from_sour_cream + money_from_whole_milk
    result = total_money
    return result

print(solution())