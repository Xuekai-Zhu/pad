def solution():
    husband_savings_per_week = 335
    wife_savings_per_week = 225
    weeks_per_month = 4
    months = 6
    total_savings = (husband_savings_per_week + wife_savings_per_week) * weeks_per_month * months
    half_savings = total_savings / 2
    number_of_children = 4
    amount_per_child = half_savings / number_of_children
    result = amount_per_child
    return result

print(solution())