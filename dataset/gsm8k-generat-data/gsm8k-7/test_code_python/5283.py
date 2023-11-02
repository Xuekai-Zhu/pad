def solution():
    total_cost = 40
    tax_rate = 0.05
    discount = 8

    # Calculate the amount of taxes paid
    taxes = total_cost * tax_rate

    # Calculate the total cost after taxes and discount
    final_cost = total_cost + taxes - discount

    # Calculate how much Cody paid (split equally with friend)
    cody_paid = final_cost / 2
    result = cody_paid
    return result

print(solution())