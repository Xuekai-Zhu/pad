def solution():
    total_students = 240
    read_three_or_more = total_students * (1/6)
    read_two = total_students * (35/100)
    read_one = total_students * (5/12)

    # Calculate the number of students who don't read novels
    no_read = total_students - (read_three_or_more + read_two + read_one)
    result = no_read
    return result

print(solution())