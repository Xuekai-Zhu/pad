def solution():
    # Define the regular seminar fee and the discount
    seminar_fee = 150
    discount_percentage = 0.05

    # Calculate the discounted fee
    discounted_fee = seminar_fee - (seminar_fee * discount_percentage)

    # Calculate the cost for 10 teachers
    cost_per_teacher = discounted_fee + 10
    total_cost = cost_per_teacher * 10

    result = total_cost
    return result

print(solution())