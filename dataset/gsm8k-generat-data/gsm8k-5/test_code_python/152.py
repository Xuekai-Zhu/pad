def solution():
    normal_cost = 80  # A subscription normally costs $80
    discount = 0.45  # The subscription is offered with a 45% discount

    # Calculate the discounted subscription cost
    discounted_cost = normal_cost * (1 - discount)
    result = discounted_cost
    return result

print(solution())