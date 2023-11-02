def solution():
    # Regular seminar fee
    regular_fee = 150

    # Discount for early registration
    early_reg_discount = 0.05

    # Number of teachers registered
    num_teachers = 10

    # Food allowance per teacher
    food_allowance = 10

    # Calculate total seminar fee with early registration discount
    discounted_fee = regular_fee - (regular_fee * early_reg_discount)

    # Total seminar fee for all teachers
    seminar_fee = discounted_fee * num_teachers

    # Total cost including food allowance
    total_cost = seminar_fee + (num_teachers * food_allowance)

    result = total_cost
    return result

print(solution())