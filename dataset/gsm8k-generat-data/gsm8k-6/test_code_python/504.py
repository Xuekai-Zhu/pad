def solution():
    # Calculate the total amount of money Sam made from yard work
    total_money = 460

    # Calculate his hourly rate
    hourly_rate = total_money / 23

    # Calculate the money he made from the 8 hours of work from September to February
    money_from_second_period = hourly_rate * 8

    # Calculate the amount of money he has left after fixing his car
    money_left = total_money + money_from_second_period - 340

    # Calculate the amount of money he still needs to save for the video game console
    money_needed = 600 - money_left

    # Calculate the number of hours he needs to work to save up the remaining money
    hours_needed = money_needed / hourly_rate

    result = hours_needed
    return result

print(solution())