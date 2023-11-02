def solution():
    regular_price = 2000  # The regular price of the ticket is $2000
    student_discount = 0.3  # Travis gets a 30% discount as he is a student

    # Calculate the discounted price that Travis needs to pay
    discounted_price = regular_price * (1 - student_discount)

    result = discounted_price
    return result

print(solution())