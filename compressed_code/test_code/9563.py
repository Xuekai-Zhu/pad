def solution():
    
    num_teachers = 10
    seminar_fee = 150
    discount_percent = 5
    discount_amount = seminar_fee * (discount_percent / 100)
    discounted_fee = seminar_fee - discount_amount
    food_allowance = 10
    total_cost = (discounted_fee * num_teachers) + (food_allowance * num_teachers)
    result = total_cost
    return result

print(solution())