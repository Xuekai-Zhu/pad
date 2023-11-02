def solution():
    # Calculate the cost of the flashlight
    hoodie_cost = 80
    flashlight_cost = 0.2 * hoodie_cost

    # Calculate the discounted price of the boots
    boots_cost = 110
    discount = 0.1
    discounted_boots_cost = boots_cost - discount * boots_cost

    # Calculate the total cost
    total_cost = hoodie_cost + flashlight_cost + discounted_boots_cost
    result = total_cost
    return result

print(solution())