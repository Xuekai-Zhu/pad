def solution():
    # Calculate the total cost of the cooking gear without the discount
    total_cost = (14 + 16 + 10*3 + 2*10*3)  # cost of hand mitts, apron, utensils, and knife
    # Calculate the discounted cost of the cooking gear
    discounted_cost = 0.75 * total_cost  # 25% off sale
    result = discounted_cost
    return result

print(solution())