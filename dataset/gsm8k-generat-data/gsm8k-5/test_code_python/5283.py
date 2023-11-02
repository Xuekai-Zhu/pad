def solution():
    # Calculate the tax and discount amounts
    tax = 0.05 * 40  # 5% tax on $40
    discount = 8

    # Calculate the total cost after tax and discount
    total_cost = 40 + tax - discount

    # Calculate the amount Cody paid after splitting the cost with his friend
    cody_paid = total_cost / 2
    result = cody_paid
    return result

print(solution())