def solution():
    num_applicants = 20000
    acceptance_rate = 0.05
    attendance_rate = 0.9

    # Calculate the number of students accepted to Harvard
    num_accepted = num_applicants * acceptance_rate

    # Calculate the number of students who choose to attend Harvard
    num_attending = num_accepted * attendance_rate
    result = num_attending
    return result

print(solution())