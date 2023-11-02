def solution():
    # Calculate the total number of tires needed
    tires_needed = (4 * 4) + (6 * 4)  # 4 cars in the shop with 4 tires each, and 6 new customers with 4 tires each

    # Calculate the number of tires that were actually changed
    tires_changed = (6 * 4) - (2 * 2)  # 6 customers with 4 tires each, minus 2 customers who only wanted half their tires changed

    # Calculate the number of customers who did not want their tires changed
    customers_not_changing = (tires_needed - tires_changed - 20) // 4

    result = customers_not_changing
    return result

print(solution())