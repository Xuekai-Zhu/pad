def solution():
    # Calculate the amount of taxes Cody paid
    taxes = 0.05 * 40  

    # Calculate the final price after taxes and discount
    final_price = (40 + taxes) - 8  

    # Calculate how much Cody paid
    cody_paid = final_price / 2  

    result = cody_paid
    return result

print(solution())