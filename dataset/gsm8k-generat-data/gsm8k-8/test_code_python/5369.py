def solution():
    # Calculate the total area of the peanut plantation
    total_area = 500 * 500

    # Calculate the total weight of peanuts produced
    total_weight = total_area * 50

    # Calculate the weight of peanut butter that can be made
    pb_weight = total_weight / 20 * 5

    # Calculate the total revenue from peanut butter sales
    revenue = pb_weight / 1000 * 10

    result = revenue
    return result

print(solution())