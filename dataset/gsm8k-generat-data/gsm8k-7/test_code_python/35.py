def solution():
    total_students = 60
    percent_below_B = 40
    num_below_B = total_students * (percent_below_B / 100)

    # Calculate the number of students who got a final grade of B and above
    num_B_and_above = total_students - num_below_B
    result = num_B_and_above
    return result

print(solution())