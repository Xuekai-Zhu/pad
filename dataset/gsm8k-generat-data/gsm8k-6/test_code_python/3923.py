def solution():
    # Calculate the total cost of repairs
    bike_cost = 80
    repair_cost = 0.25 * bike_cost
    total_cost = bike_cost + repair_cost

    # Calculate the total revenue Reginald earned from selling apples
    revenue = total_cost / (1/4)  # Reginald earned 1/4 profit from selling apples
    num_apples = revenue / 1.25  # Reginald sells each apple for $1.25 

    # Calculate the number of apples remaining after the repairs are paid for
    remaining_apples = num_apples / 5

    result = remaining_apples
    return result

print(solution())