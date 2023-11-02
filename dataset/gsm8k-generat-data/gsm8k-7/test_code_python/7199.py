def solution():
    paint_pay = 5
    sell_pay = paint_pay + 8
    num_bikes = 8

    # Calculate the total pay for painting the bikes
    paint_total = paint_pay * num_bikes

    # Calculate the total pay for selling the bikes
    sell_total = sell_pay * num_bikes

    # Calculate the total pay for painting and selling the bikes
    total_pay = paint_total + sell_total
    result = total_pay
    return result

print(solution())