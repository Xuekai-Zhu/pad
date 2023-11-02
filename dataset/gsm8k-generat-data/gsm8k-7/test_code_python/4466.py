def solution():
    num_floors = 3
    windows_per_floor = 3
    payment_per_window = 2
    discount_per_3_days = 1
    days_worked = 6

    # Calculate the total number of windows in the house
    total_windows = num_floors * windows_per_floor

    # Calculate the initial payment for cleaning all the windows
    initial_payment = total_windows * payment_per_window

    # Calculate the number of 3-day periods that have passed
    num_discount_periods = days_worked // 3

    # Calculate the total discount for taking too long to clean the windows
    total_discount = num_discount_periods * discount_per_3_days

    # Calculate the final payment, after subtracting the discount
    final_payment = initial_payment - total_discount

    result = final_payment
    return result

print(solution())