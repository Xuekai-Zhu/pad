def solution():
    # Calculate the total amount of money raised by the students
    total_student_money = 20 * 5  # each student contributed $5 dollars

    # Calculate the total cost of the trip
    total_trip_cost = 20 * 7  # the cost of the trip is $7 for each student

    # Calculate the amount of money left in Miss Grayson's class fund
    left_over_money = 50 + total_student_money - total_trip_cost

    result = left_over_money
    return result

print(solution())