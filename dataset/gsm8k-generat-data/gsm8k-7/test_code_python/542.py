def solution():
    cakes_per_day = 10
    num_days = 5
    cakes_baked = cakes_per_day * num_days

    cakes_eaten = 12

    # Calculate the remaining cakes
    remaining_cakes = cakes_baked - cakes_eaten

    frosting_per_cake = 2

    # Calculate the total cans of frosting needed
    total_frosting = remaining_cakes * frosting_per_cake
    result = total_frosting
    return result

print(solution())