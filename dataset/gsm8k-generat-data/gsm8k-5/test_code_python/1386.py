def solution():
    # Calculate the total number of tires needed
    total_tires = (4 * 4) + (6 * 4)  # 4 cars with 4 tires each, and 6 customers with 4 tires each

    # Subtract the number of tires the two customers wanted half changed
    total_tires -= 2 * 2

    # Calculate the number of tires actually changed
    tires_changed = total_tires - 20

    # Calculate the number of customers who did not want their tires changed
    customers_not_changing = (total_tires - tires_changed) // 4 - 4  # Subtract the original 4 cars

    result = customers_not_changing
    return result

print(solution())