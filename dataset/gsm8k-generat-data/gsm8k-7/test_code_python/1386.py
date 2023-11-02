def solution():
    num_cars_in_shop = 4
    num_customers = 6
    total_customers = num_cars_in_shop + num_customers

    num_tires_per_car = 4
    total_tires_needed = total_customers * num_tires_per_car

    # Calculate the number of tires that will not be changed
    tires_not_changed = 0

    # Two customers want half of their tires changed, so that's 4 tires not changed
    tires_not_changed += 4

    # For the remaining customers, assume all their tires will be changed
    tires_changed = total_tires_needed - tires_not_changed

    # Calculate the number of tires that were bought
    num_tires_bought = tires_changed + 20  # 20 tires left at the end of the week

    # Calculate the number of customers who did not want their tires changed
    num_customers_not_changed = tires_not_changed / num_tires_per_car

    result = num_customers_not_changed
    return result

print(solution())