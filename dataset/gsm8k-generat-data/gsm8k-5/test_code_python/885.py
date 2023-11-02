def solution():
    mold_cost = 250  # The cobbler charges $250 to make the mold
    work_time = 8  # The cobbler takes 8 hours to make the shoes
    work_cost_per_hour = 75  # The cobbler charges $75 an hour to make the shoes
    first_pair_discount = 0.8  # The cobbler gives Bobby an 80% discount on the cost of making the shoes

    # Calculate the total cost of making the shoes
    work_cost = work_time * work_cost_per_hour
    total_cost = mold_cost + work_cost
    discount_amount = first_pair_discount * total_cost
    final_cost = total_cost - discount_amount
    result = final_cost
    return result

print(solution())