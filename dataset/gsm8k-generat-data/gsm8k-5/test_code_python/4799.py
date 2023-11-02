def solution():
    num_teachers = 10  # The school registered 10 teachers
    seminar_fee = 150  # The regular seminar fee is $150
    discount_percent = 5  # They offer a 5% discount if they register 2 days before the scheduled seminar
    food_allowance = 10  # The school released a $10 food allowance for each of the teachers

    # Calculate the total seminar fee with discount
    discount_amount = (discount_percent / 100) * seminar_fee
    discounted_fee = seminar_fee - discount_amount

    # Calculate the total amount spent by the school
    total_fee = num_teachers * discounted_fee
    total_spending = total_fee + (food_allowance * num_teachers)
    result = total_spending
    return result

print(solution())