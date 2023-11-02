def solution():
    # Calculate the total amount of milk sold in each container size
    two_liter_containers = 3 * 2
    three_quarter_liter_containers = 2 * 0.75
    half_liter_containers = 5 * 0.5

    # Calculate the total amount of milk sold in liters
    total_milk_sold = two_liter_containers + three_quarter_liter_containers + half_liter_containers

    result = total_milk_sold
    return result

print(solution())