def solution():
    # Calculate the cost of the hoodie
    hoodie_cost = 80

    # Calculate the cost of the flashlight as 20% of the hoodie cost
    flashlight_cost = 0.2 * hoodie_cost

    # Calculate the discounted cost of the boots
    boots_cost = 110 * 0.9

    # Calculate the total cost
    total_cost = hoodie_cost + flashlight_cost + boots_cost
    result = total_cost
    return result

print(solution())