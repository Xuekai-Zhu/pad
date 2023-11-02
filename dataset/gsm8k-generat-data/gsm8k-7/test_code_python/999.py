def solution():
    class_fund = 50
    num_students = 20
    student_contribution = 5
    trip_cost_per_student = 7

    # Calculate the total amount contributed by the students
    total_student_contribution = num_students * student_contribution

    # Calculate the total cost of the trip
    total_trip_cost = num_students * trip_cost_per_student

    # Calculate the remaining amount in the class fund after paying for the trip
    remaining_class_fund = class_fund + total_student_contribution - total_trip_cost
    result = remaining_class_fund
    return result

print(solution())