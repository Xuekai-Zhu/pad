def solution():
    total_marks = 50
    first_ten_marks = 90
    fifteen_marks = first_ten_marks - 10
    last_thirty_marks = 60
    average_marks = (first_ten_marks + fifteen_marks + last_thirty_marks) / total_marks
    return average_marks

print(solution())