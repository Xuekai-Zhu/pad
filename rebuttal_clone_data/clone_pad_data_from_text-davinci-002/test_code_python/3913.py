def solution():
    current_speed = 10
    current_bill = 20
    new_speed_1 = 20
    new_speed_2 = 30
    new_bill_1 = current_bill + 10
    new_bill_2 = (current_bill * 2) + 10
    difference = new_bill_2 - new_bill_1
    per_year_savings = difference * 12
    result = per_year_savings
    return result

print(solution())