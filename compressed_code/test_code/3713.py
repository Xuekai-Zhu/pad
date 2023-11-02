def solution():
    
    seminar_fee = 150
    discount = 0.05
    registration_fee = seminar_fee - (seminar_fee * discount)
    num_teachers = 10
    food_allowance = 10
    total_fee = (registration_fee + food_allowance) * num_teachers
    result = total_fee
    return result

print(solution())