def solution():
    """The school auditorium has 4 rows of seats. There are 18 seats in each row. One-fourth of the seats were occupied by the administrators. One-third of the remaining seats were occupied by the parents and the rest were occupied by the students. How many students were there in the school auditorium?"""
    total_seats = 4 * 18
    admin_seats = total_seats // 4
    remaining_seats = total_seats - admin_seats
    parent_seats = remaining_seats // 3
    student_seats = remaining_seats - parent_seats
    result = student_seats
    return result

print(solution())