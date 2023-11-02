def solution():
    total_students = 280  # Total number of students in the class
    # Let's denote the number of students present on day one as "x"
    x = total_students / 3  # Since we're considering three days

    # Number of students present on the second day
    y = x + 40  # 40 more than the first day

    # Number of students absent on the second day
    z = 2 * (x - (total_students / 7))  # Twice the number absent on the third day

    # Total number of absent students in the three days
    total_absent = z + (total_students - (x + y))  # Students absent on first and third days
    result = total_absent
    return result

print(solution())