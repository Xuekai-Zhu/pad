def solution():
    candy_bar_price = 2  # Candy bars cost $2 each
    chips_price = 0.5  # Chips cost $0.50 each
    num_students = 5  # There are 5 students buying snacks

    # Calculate the total cost of candy bars and chips for one student
    one_student_cost = (1 * candy_bar_price) + (2 * chips_price)

    # Calculate the total cost for all 5 students
    total_cost = one_student_cost * num_students
    result = total_cost
    return result

print(solution())