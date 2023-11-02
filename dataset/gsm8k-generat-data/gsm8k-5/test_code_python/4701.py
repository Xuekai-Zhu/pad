def solution():
    regular_admission = 8  # Admission costs $8
    discount = 3  # The price is $3 less before 6 P.M.
    discounted_admission = regular_admission - discount  # Discounted admission price
    num_people = 2 + 3  # Kath takes 2 siblings and 3 friends
    total_discounted_admission = discounted_admission * num_people  # Total cost for discounted admission

    # Kath has to pay regular admission for herself
    total_cost = regular_admission + total_discounted_admission
    result = total_cost
    return result

print(solution())