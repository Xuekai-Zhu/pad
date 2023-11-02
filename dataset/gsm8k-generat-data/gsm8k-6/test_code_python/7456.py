def solution():
    # Calculate the total cost of fruits before discounts
    total_cost = 5*1 + 3*2 + 2*3  # 5 apples, 3 oranges, and 2 bananas

    # Calculate the number of 5-fruit sets Mary bought
    num_sets = (5+3+2) // 5

    # Calculate the total discount Mary receives
    total_discount = num_sets * 1

    # Calculate the final cost after discounts
    final_cost = total_cost - total_discount

    result = final_cost
    return result

print(solution())