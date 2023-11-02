def solution():
    weekday_price = 0.5  # The price of the newspaper on Wednesday, Thursday, and Friday
    sunday_price = 2  # The price of the newspaper on Sunday
    num_weekdays = 3*3  # Hillary buys newspapers on Wednesday, Thursday, and Friday for 3 weeks
    num_sundays = 8  # Hillary buys newspapers on Sunday for 8 weeks

    # Calculate the total amount Hillary spends on newspapers over 8 weeks
    total_cost = (weekday_price * num_weekdays) + (sunday_price * num_sundays)
    result = total_cost
    return result

print(solution())