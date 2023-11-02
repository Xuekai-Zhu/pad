def solution():
    bonus_amount = 1496  # bonus received by Ben
    kitchen_amount = bonus_amount/22  # amount allocated for kitchen
    holidays_amount = bonus_amount/4  # amount allocated for holidays
    children_gifts_amount = bonus_amount/8/3  # amount allocated for each child's gift
    total_expenses = kitchen_amount + holidays_amount + children_gifts_amount*3  # total amount of expenses
    remaining_amount = bonus_amount - total_expenses  # remaining amount after expenses
    result = remaining_amount
    return result

print(solution())