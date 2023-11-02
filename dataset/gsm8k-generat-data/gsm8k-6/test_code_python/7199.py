def solution():
    # Calculate the amount Henry is paid to paint one bike
    paint_payment = 5

    # Calculate the amount Henry is paid to sell one bike
    sell_payment = paint_payment + 8

    # Calculate total payment for selling and painting 8 bikes
    total_payment = (sell_payment + paint_payment) * 8

    result = total_payment
    return result

print(solution())