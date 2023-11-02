def solution():
    regular_fee = 150
    discount = 5
    discount_amount = regular_fee * (discount / 100)
    two_days_fee = regular_fee - discount_amount
    num_teachers = 10
    food_allowance = 10
    total_spent = (two_days_fee * num_teachers) + (food_allowance * num_teachers)
    result = total_spent
    return result

print(solution())