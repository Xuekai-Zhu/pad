def solution():
    total_cost = 67
    coupon = 4
    num_people = 3

    # Calculate the total cost after applying the coupon
    discounted_cost = total_cost - coupon

    # Calculate the cost per person
    cost_per_person = discounted_cost / num_people
    result = cost_per_person
    return result

print(solution())