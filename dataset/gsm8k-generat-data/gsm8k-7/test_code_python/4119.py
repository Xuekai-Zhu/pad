def solution():
    month_one = 350
    month_two = (2 * month_one) + 50
    month_three = 4 * (month_one + month_two)

    total_pay = month_one + month_two + month_three
    result = total_pay
    return result

print(solution())